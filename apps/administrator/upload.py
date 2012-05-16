from photo_manager.models import Album, Photo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
import os
import random
from django.http import HttpResponse
from hadrian.contrib.locations.models import Location
from django.core.urlresolvers import reverse
from photo_manager.tasks import ThumbnailTask 
from conf import defaults
from django.conf import settings as app_settings
from sorl.thumbnail import get_thumbnail
from django.core.files.uploadedfile import UploadedFile

#importing json parser to generate jQuery plugin friendly json response
from django.utils import simplejson


def upload_photo(request, location_slug, album_slug, user_id):
    context = {}
    if request.method == 'POST':
        #
        uploaded_file = request.FILES[u'file']
        
        # write the file into /tmp
        num1 = str(random.randint(0, 1000000))
        num2 = str(random.randint(1001, 9000000))
        
        ext = os.path.splitext(uploaded_file.name)[1]
        filename = str(num1 + num2) + ext
        wrapped_file = UploadedFile(uploaded_file)
        file_size = wrapped_file.file.size
        
        album_used = get_object_or_404(Album, slug=album_slug)
        photo_new = Photo(title=filename, album=album_used)
        photo_new.file_name = filename
        photo_new.image = 'images/' + filename
        # Set location to default location
        photo_new.location = get_object_or_404(Location, slug=location_slug)
        user = get_object_or_404(User, pk=user_id)
        photo_new.user = user
        photo_new.save()
            
        destination_path = app_settings.PHOTO_DIRECTORY + '/%s' % (filename)   
        destination = open(destination_path, 'wb+')
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
        destination.close()
        
        im = get_thumbnail(photo_new.image, "80x80", quality=50)
        thumb_url = im.url
        
        ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
        if ENABLE_CELERY:
            ThumbnailTask.delay(photo_new.id)
            
        # JQuery upload requires that you respond with JSON
        # Somethign like this..
        result = []
        result.append({"name":filename, 
                       "size":file_size, 
                       "url":"/where/does/this/go", 
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
    
        return render(request,'administrator/add_photos.html', context)
        
        
def upload_delete(request, pk):
    return render(request, "example.html")