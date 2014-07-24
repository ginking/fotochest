from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.http import HttpResponse

from locations.models import *

from .models import Photo, Album

__authors__ = "Derek Stegelman"
__date__ = "August 2012"


class AlbumDetailView(ListView):
    """

    """
    model = Album
    paginate_by = 12
    template_name = 'photo_manager/albums.html'

    def get_album(self):
        return Album.objects.get(slug=self.kwargs.get('album_slug'))

    def get(self, *args, **kwargs):
        if self.get_album().child_albums:
            self.queryset = self.get_album().child_albums
            self.paginate_by = 8
            self.context_object_name = 'albums'
        else:
            self.queryset = Photo.objects.active().filter(album__slug=self.get_album().slug)
            self.paginate_by = 12
            self.context_object_name = 'photos'

        return super(AlbumDetailView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['album_view'] = True
        context['album'] = self.get_album()
        return context


class AlbumListView(ListView):
    context_object_name = "albums"
    template_name = "photo_manager/albums.html"
    queryset = Album.objects.parent_albums()
    paginate_by = 12


class HomepageListView(ListView):
    context_object_name = "photos"
    template_name = "photo_manager/index.html"
    paginate_by = 12

    def get_queryset(self):
        return Photo.objects.active()


class PhotoDetailView(DetailView):
    queryset = Photo.objects.filter(deleted=False)
    slug_url_kwarg = 'photo_slug'
    pk_url_kwarg = 'photo_id'
    context_object_name = "photo"
    template_name = "photo_manager/photo.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        photo = self.get_object()
        context['photo_id'] = photo.id
        context['other_photos'] = Photo.objects.active().filter(album=photo.album, id__lt=photo.id)[:9]
        context['photos_from_this_location'] = Photo.objects.active().filter(location=photo.location)[:6]
        return context


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
    slug_url_kwarg = 'photo_slug'
    template_name = "photo_manager/fullscreen.html"

    
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
