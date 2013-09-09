from sorl.thumbnail import get_thumbnail

from django.core.files.uploadedfile import UploadedFile
from django.utils import simplejson
from django.conf import settings as app_settings
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from hadrian.contrib.locations.models import Location

from administrator.tasks import thumbnail_task
from administrator.utils import get_randomized_file_name
import defaults
from photo_manager.models import Album, Photo

def create_photo(album_slug, filename, location_slug, user_id):
    try:
        album = Album.objects.get(slug=album_slug)
    except Album.DoesNotExist:
        raise Exception("Album does not exist.")

    try:
        location = Location.objects.get(slug=location_slug)
    except Location.DoesNotExist:
        raise Exception("Location does not exist.")
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Exception("User does not exist.")

    photo = Photo(title=filename, album=album,
                  file_name=filename, image='images/%s' % filename,
                  location=location, user=user)
    photo.save()
    return photo


def upload_photo(request, location_slug, album_slug, user_id):
    """ Upload the photos!
    """
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES[u'file']

        filename = get_randomized_file_name(uploaded_file.name)

        wrapped_file = UploadedFile(uploaded_file)
        file_size = wrapped_file.file.size
        photo_new = create_photo(album_slug, filename, location_slug, user_id)

        destination_path = app_settings.MEDIA_ROOT + '/images/%s' % (filename)
        destination = open(destination_path, 'wb+')
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
        destination.close()
        
        im = get_thumbnail(photo_new.image, "80x80", quality=50)
        thumb_url = im.url
        
        ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
        if ENABLE_CELERY:
            thumbnail_task.delay(photo_new)
            
        # JQuery upload requires that you respond with JSON
        # Somethign like this..
        result = []
        result.append({"name":filename, 
                       "size":file_size, 
                       "url": "%s%s" % (app_settings.MEDIA_URL, photo_new.image), 
                       "thumbnail_url":thumb_url,
                       "delete_url":reverse('upload_delete', args=[photo_new.pk]), 
                       "delete_type":"POST",})
        response_data = simplejson.dumps(result)
        
        #checking for json data type
        #big thanks to Guy Shapiro
        if "application/json" in request.META['HTTP_ACCEPT_ENCODING']:
            mimetype = 'application/json'
        else:
            mimetype = 'text/plain'
        return HttpResponse(response_data, mimetype=mimetype)
        
    else:
        
        context['album_slug'] = album_slug
        context['location_slug'] = location_slug
    
        return render(request, 'administrator/add_photos.html', context)


def upload_delete(request, pk):
    return render(request, "example.html")