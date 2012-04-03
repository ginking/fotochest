from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from photo_manager.models import *
from locations.models import *
from locations.forms import *
from profiles.models import get_locations_for_user
from django.contrib.auth.models import User
import os
from django.conf import settings
import random
from sorl.thumbnail import get_thumbnail
import sorl
from PIL import Image
from photo_manager.forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from photo_manager.tasks import ThumbnailTask


def choose(request):
    return redirect('file_uploader', username=request.user.username, location_slug=request.GET.get('location'), album_slug=request.GET.get("album"))

#--------------------------------------------#
#
# photo_upload().  Tired as I write this.  the
# method should add photos to a specific location
# THIS NEEDS FIXING
#
#--------------------------------------------#
@csrf_exempt
def photo_upload(request, username, location_slug, album_slug):
    context = {}
        
    if request.method == 'POST':
        for field_name in request.FILES:
            uploaded_file = request.FILES[field_name]
            
            # write the file into /tmp
            num1 = str(random.randint(0, 1000000))
            num2 = str(random.randint(1001, 9000000))
            
            ext = os.path.splitext(uploaded_file.name)[1]
            filename = str(num1 + num2) + ext
            album_used = get_object_or_404(Album, slug=album_slug)
            
            photo_new = Photo(title=filename, album=album_used)
            photo_new.file_name = filename
            photo_new.image = 'images/' + filename
            # Set location to default location
            photo_new.location = get_object_or_404(Location, slug=location_slug)
            photo_new.user = get_object_or_404(User, username=username)
            photo_new.save()
            destination_path = settings.PHOTO_DIRECTORY + '/%s' % (filename)   
            destination = open(destination_path, 'wb+')
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
            destination.close()
            ThumbnailTask.delay(photo_new.id)
            
        # indicate that everything is OK for SWFUpload
        
        return HttpResponse("ok", mimetype="text/plain")
        
    else:
        if request.user and request.user.username == username:
            user = get_object_or_404(User, username=username)
            context['current_user'] = user
            context['user_page'] = '1'
            context['upload_dir'] = settings.PHOTO_DIRECTORY
            context['album_slug'] = album_slug
            context['location_slug'] = location_slug
            context['domain_static'] = settings.DOMAIN_STATIC    
            return render(request,'%s/upload.html' % settings.ACTIVE_THEME, context)
        else:
            return render(request, 'not_authorized.html')


### Forms
@login_required
def edit_photo(request, photo_id, album_slug=None, username=None, photo_slug=None):
    context = {}
    context['current_user'] = get_object_or_404(User, username=username)
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
    if request.user != photo.user:
        return render(request, '%s/not_authorized.html' % settings.ACTIVE_THEME)
        
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            
            return redirect(new_photo)
    else:        
        form = PhotoForm(instance=photo)
    context['form'] = form
    context['photo'] = photo
    context['exif_data'] = photo.get_exif_data()
    return render(request, '%s/edit_photo.html' % settings.ACTIVE_THEME, context)

@login_required    
def delete_photo(request, photo_id, album_slug=None, username=None, photo_slug=None):
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
    if request.user != photo.user:
        return render(request, '%s/not_authorized.html' % settings.ACTIVE_THEME)
    
    photo.deleted = True
    photo.save()
    #@todo - This needs to point somewhere else after deletion..
    return render(request, '%s/edit_photo.html' % settings.ACTIVE_THEME)
    
@login_required
def rotate_photo(request, photo_id, rotate_direction, album_slug=None, username=None, photo_slug=None):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.user:
        return render(request, 'not_authorized.html')
    im = Image.open(photo.image)
    if rotate_direction == "counter":
        rotate_image = im.rotate(90)
    else:
        rotate_image = im.rotate(270)
    rotate_image.save(photo.image.file.name, overwrite=True)
    sorl.thumbnail.delete(photo.image, delete_file=False)
    photo.make_thumbnails()
    return redirect(photo.get_absolute_url())
