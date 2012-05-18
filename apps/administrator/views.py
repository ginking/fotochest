from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from photo_manager.models import Photo, Album
from administrator.models import Settings
from administrator.forms import SettingsForm
from hadrian.contrib.locations.models import *
from hadrian.contrib.locations.forms import *
from django.contrib.auth.models import User
import os
from django.conf import settings as app_settings
import random
import sorl
from PIL import Image
from photo_manager.forms import *
from django.contrib.auth.decorators import login_required
from photo_manager.tasks import ThumbnailTask
from photo_manager.forms import AlbumForm
from conf import defaults
from django.contrib import messages
from django.http import HttpResponse

@login_required
def add_photos(request):
    context = {}
    return render(request, "administrator/add_photos.html", context)

def get_size(start_path = '%s/images' % app_settings.MEDIA_ROOT):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size

@login_required
def dashboard(request):
    photos = Photo.objects.active()
    albums = Album.objects.filter(parent_album=None)
    context = {'albums': albums}
    context['total_photos'] = Photo.objects.filter(deleted=False).count()
    context['total_albums'] = albums.count()
    context['total_locations'] = Location.objects.all().count()
    context['total_size'] = convert_bytes(get_size())
    paginator = Paginator(photos, 16)
    page = request.GET.get('page', 1)
    
    try:
        context['photos'] = paginator.page(page)
    except PageNotAnInteger:
        context['photos'] = paginator.page(1)
    except EmptyPage:
        context['photos'] = paginator.page(paginator.num_pages)
    context['paginator'] = paginator
    # Add pagination
    return render(request, "administrator/dashboard.html", context)

@login_required
def album_list(request):
    albums = Album.objects.all()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid:
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            messages.add_message(request, messages.SUCCESS, "New Album Saved.")
            return redirect("administrator.views.album_list")
    else:
        form = AlbumForm()
    context = {'albums':albums, 'album_form':form}
    return render(request, "administrator/albums.html", context)

@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {}
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
    else:
        form = AlbumForm(instance=album)
        
    context['album_form'] = form
    context['album'] = album
    return render(request, "administrator/album_detail.html", context)

@login_required
def album_photo_details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album':album}
    #Fix this Add pagination
    return render(request, "administrator/", context)

@login_required
def add_location(request):
    context = {}
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("administrator.views.locations")
    else:
        form = LocationForm()
    context['form'] = form    
    return render(request, "administrator/add_location.html", context) 

@login_required
def settings(request):
    context = {}
    setting = get_object_or_404(Settings, pk=1)
    if request.method == "POST":
        form = SettingsForm(request.POST, instance=setting)
        if form.is_valid():
            setting = form.save()
            messages.add_message(request, messages.SUCCESS, "Settings Updated.")
            return redirect("administrator.views.settings")
    else:
        form = SettingsForm(instance=setting)
    context['form'] = form
    return render(request, "administrator/settings.html", context)

@login_required
def locations(request, username=None):
    context = {}
    context['locations'] = Location.objects.all()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("administrator.views.locations")
    else:
        form = LocationForm()
    context['form'] = form  
    return render(request, "administrator/locations.html", context)

def choose(request):
    return redirect('file_uploader', location_slug=request.GET.get('location'), album_slug=request.GET.get("album"), user_id=request.GET.get('user_id'))

#--------------------------------------------#
#
# photo_upload().  Tired as I write this.  the
# method should add photos to a specific location
# THIS NEEDS FIXING
#
#--------------------------------------------#
@csrf_exempt
def photo_upload(request, location_slug, album_slug, user_id):
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
            user = get_object_or_404(User, pk=user_id)
            photo_new.user = user
            photo_new.save()
            destination_path = app_settings.PHOTO_DIRECTORY + '/%s' % (filename)   
            destination = open(destination_path, 'wb+')
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
            destination.close()
            ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
            if ENABLE_CELERY:
                ThumbnailTask.delay(photo_new.id)
            print "IT WORKED"
        # indicate that everything is OK for SWFUpload
        
        return HttpResponse("ok", mimetype="text/plain")
        
    else:
        
        context['upload_dir'] = app_settings.PHOTO_DIRECTORY
        context['album_slug'] = album_slug
        context['location_slug'] = location_slug
        context['domain_static'] = app_settings.DOMAIN_STATIC    
        return render(request,'administrator/add_photos.html', context)


### Forms
@login_required
def edit_photo(request, photo_id):
    context = {}
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
        
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Photo %s saved" % photo.title)
            
            return redirect('administrator.views.dashboard')
        else:
            print form.errors
            print("poop")
    else:
        messages.add_message(request, messages.ERROR, "ERROR")
            
        return redirect('administrator.views.dashboard')


@login_required    
def delete_photo(request, photo_id, album_slug=None, username=None, photo_slug=None):
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)    
    photo.deleted = True
    photo.save()
    #@todo - This needs to point somewhere else after deletion..
    messages.add_message(request, messages.SUCCESS, "Photo %s deleted" % photo.title)
    return render(request, 'administrator/dashboard.html' % app_settings.ACTIVE_THEME)
    
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

@login_required
def build_thumbnails(request):
    from conf import defaults
    ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
    from photo_manager.tasks import ThumbnailTask
    for photo in Photo.objects.all():
        photo.thumbs_created = False
        photo.save()
        if ENABLE_CELERY:
            ThumbnailTask.delay(photo.id)
    messages.add_message(request, messages.SUCCESS, "Job queued.")
    return redirect('admin_utilities')
    
   
@login_required
def delete_thumbnails(request):
    from administrator.tasks import ThumbnailCleanupTask
    for photo in Photo.objects.all():
        ThumbnailCleanupTask.delay(photo.id)
    messages.add_message(request, messages.SUCCESS, "Thumbs deleted.")
    return redirect('admin_utilities')
