from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from fotochest.photo_manager.models import Photo, Album
from hadrian.contrib.locations.models import *
from django.conf import settings
from django.http import HttpResponse

__authors__ = "Derek Stegelman"
__date__ = "August 2012"

def album(request, album_id, album_slug):
    context = {}
    context['album_slug'] = album_slug
    context['album_view'] = True
    # If it has child albums, show those, if not, show pictures.
    album = get_object_or_404(Album, pk=album_id)
    context['album'] = album
    if album.has_child_albums == True:
        # Show child albums
        albums = Album.objects.filter(parent_album=album)
        paginator = Paginator(albums, 6)
        page = request.GET.get('page', 1)
        try:
            context['child_albums'] = paginator.page(page)
        except PageNotAnInteger:
            context['child_albums'] = paginator.page(1)
        except EmptyPage:
            context['child_albums'] = paginator.page(paginator.num_pages)
        
        context['paginator'] = paginator
    
    photos = Photo.objects.active().filter(album__slug=album_slug)
    photo_paginator = Paginator(photos, 12)
    photo_page = request.GET.get('page', 1)
    try:
        context['photos'] = photo_paginator.page(photo_page)
    except PageNotAnInteger:
        context['photos'] = photo_paginator.page(1)
    except EmptyPage:
        context['photos'] = photo_paginator.page(photo_paginator.num_pages)
            
    return render(request, "photo_manager/albums.html", context)


class AlbumListView(ListView):
    context_object_name = "albums"
    template_name = "photo_manager/albums.html"
    queryset = Album.objects.filter(parent_album=None)
    paginate_by = 12

class HomepageListView(ListView):
    context_object_name = "photos"
    template_name = "photo_manager/index.html"
    queryset = Photo.objects.active()
    paginate_by = 12


class PhotoDetailView(DetailView):
    queryset = Photo.objects.filter(deleted=False)
    pk_url_kwarg = "photo_id"
    context_object_name = "photo"
    template_name = "photo_manager/photo.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        context['photo_id'] = self.kwargs['photo_id']
        photo = Photo.objects.get(pk=self.kwargs['photo_id'])
        context['other_photos'] = Photo.objects.active().filter(album=photo.album, id__lt=photo.id)[:9]
        context['photos_from_this_location'] = Photo.objects.active().filter(location=photo.location)[:6]
        return context

def photo(request, photo_id, album_slug=None, photo_slug=None):
    context = {}
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
    active_album = photo.album
    photos = Photo.objects.active().filter(album=active_album, id__lt=photo_id)[:9]
    context['photo_id'] = photo_id
    context['photo'] = photo
    context['other_photos'] = photos
    context['photos_from_this_location'] = Photo.objects.active().filter(location=photo.location)[:6]
    return render(request, "photo_manager/photo.html", context)

def photo_download(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    file = photo.image
    mimetype = "application/octet-stream"
    response = HttpResponse(file.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=%s" % photo.filename
    return response

class PhotoFullScreen(DetailView):
    context_object_name = 'photo'
    queryset = Photo.objects.filter(deleted=False)
    pk_url_kwarg = "photo_id"
    template_name = "photo_manager/fullscreen.html"


def slideshow(request, location_slug=None, album_slug=None):
    context = {}
    photos = Photo.objects.filter(album__slug=album_slug)[:2]
    context['initial_photos'] = photos
    all_photos = Photo.objects.filter(album__slug=album_slug)[:12]
    context['all_photos'] = all_photos
    return render(request, "photo_manager/slideshow.html", context)
    
### Map/Location views

class LocationsListView(ListView):
    context_object_name = "locations"
    template_name = "photo_manager/map.html"
    queryset = Location.objects.all()
    
class PhotoLocationsListView(ListView):
    paginate_by = 12
    template_name = "photo_manager/location.html"
    context_object_name = "photos"

    def get_queryset(self):
        location = Location.objects.get(slug=self.kwargs['location_slug'])
        return Photo.objects.filter(location=location)

    def get_context_data(self, **kwargs):
        context = super(PhotoLocationsListView, self).get_context_data(**kwargs)
        location_slug = self.kwargs['location_slug']
        location = Location.objects.get(slug=location_slug)
        context['location'] = location
        context['location_view'] = True
        context['location_slug'] = location_slug
        return context
