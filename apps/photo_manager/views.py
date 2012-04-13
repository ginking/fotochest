from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from photo_manager.models import Photo, Album
from locations.models import *
from locations.forms import *
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


def album(request, album_id, album_slug):
    context = {}
    context['album_slug'] = album_slug
    # If it has child albums, show those, if not, show pictures.
    album = get_object_or_404(Album, pk=album_id)
    if album.has_child_albums == True:
        # Show child albums
        albums = Album.objects.filter(parent_album=album)
        paginator = Paginator(albums, 6)
        page = request.GET.get('page', 1)
        try:
            context['albums'] = paginator.page(page)
        except PageNotAnInteger:
            context['albums'] = paginator.page(1)
        except EmptyPage:
            context['albums'] = paginator.page(paginator.num_pages)
        
        context['paginator'] = paginator
        if request.POST and request.user.is_authenticated():
            form = AlbumForm(request.POST)
            if form.is_valid():
                album = form.save(commit=False)
                album.user = request.user
                album.save()
        else:
            context['album_form'] = AlbumForm()
        
        return render(request, "%s/albums.html" % settings.ACTIVE_THEME, context)
    else:
        photos = Photo.objects.active().filter(album__slug=album_slug)
        paginator = Paginator(photos, 12)
        page = request.GET.get('page', 1)
        context['album_view'] = True
        try:
            context['photos'] = paginator.page(page)
        except PageNotAnInteger:
            context['photos'] = paginator.page(1)
        except EmptyPage:
            context['photos'] = paginator.page(paginator.num_pages)
            
        return render(request, "%s/index.html" % settings.ACTIVE_THEME, context)
    
def albums(request):
    context = {}
    
    albums = Album.objects.filter(parent_album=None)
    
    paginator = Paginator(albums, 12)
    page = request.GET.get('page', 1)
    
    try:
        context['albums'] = paginator.page(page)
    except PageNotAnInteger:
        context['albums'] = paginator.page(1)
    except EmptyPage:
        context['albums'] = paginator.page(paginator.num_pages)
    
    if request.POST and request.user.is_authenticated():
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
    else:
        context['album_form'] = AlbumForm()
        context['parent_albums'] = Album.objects.all()
            
    
    return render(request, "%s/albums.html" % settings.ACTIVE_THEME, context)
       
def homepage(request):
    context = {}
    
    photos = Photo.objects.active()
    context['form_albums'] = Album.objects.all()
        
    paginator = Paginator(photos, 12)
    page = request.GET.get('page', 1)
    
    try:
        context['photos'] = paginator.page(page)
    except PageNotAnInteger:
        context['photos'] = paginator.page(1)
    except EmptyPage:
        context['photos'] = paginator.page(paginator.num_pages)
    return render(request, "%s/index.html" % settings.ACTIVE_THEME, context)
    

def photo(request, photo_id, album_slug=None, photo_slug=None):
    context = {}
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
    active_album = photo.album
    photos = Photo.objects.active().filter(album=active_album, id__lt=photo_id)[:8]
    context['photo_id'] = photo_id
    context['photo'] = photo
    context['other_photos'] = photos
    context['photos_from_this_location'] = Photo.objects.active().filter(location=photo.location)[:4]
    return render(request, "%s/photo.html" % settings.ACTIVE_THEME, context)

def photo_fullscreen(request, photo_id, album_slug, photo_slug):
    context = {}
    context['photo'] = get_object_or_404(Photo, pk=photo_id, deleted=False)
    
    return render(request, '%s/fullscreen.html' % settings.ACTIVE_THEME, context)

    
def slideshow(request, location_slug=None, album_slug=None):
    context = {}
    if location_slug:
        context['photos'] = Photo.objects.active().filter(location__slug=location_slug)
        location = get_object_or_404(Location, slug=location_slug)
        context['what_object'] = location
    if album_slug:
        context['photos'] = Photo.objects.active().filter(album__slug=album_slug)
        album = get_object_or_404(Album, slug=album_slug)
        context['what_object'] = album.title
     
    
    return render(request, "%s/slideshow.html" % settings.ACTIVE_THEME, context)
    
### Map/Location views

def locations(request):
    context = {}
    

    context['locations'] = Location.objects.all()
    if request.POST:
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            if username:
                redirect("locations.views.locations", username=username)
            else:
                redirect("locations")
    else:
        context['location_form'] = LocationForm()
    
    return render(request, "%s/map.html" % settings.ACTIVE_THEME, context)
    
def location(request, location_slug):
    location = get_object_or_404(Location, slug=location_slug)
    # Get location object, now get more location objects where location.city = location.city?
    # how do we know if we are asking for city, state or country?  Should we have that specified?
    context = {}
    
    photos = Photo.objects.filter(location=location)
    paginator = Paginator(photos, 12)

    page = request.GET.get('page', 1)
    context['location_view'] = True
    context['location_slug'] = location_slug
    try:
        context['photos'] = paginator.page(page)
    except PageNotAnInteger:
        context['photos'] = paginator.page(1)
    except EmptyPage:
        context['photos'] = paginator.page(paginator.num_pages)
    return render(request, "%s/index.html" % settings.ACTIVE_THEME, context)  
    

    