import sorl

from PIL import Image

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView
from django.conf import settings as app_settings
from django.contrib.auth.decorators import login_required

from locations.models import *
from locations.forms import *

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from fotochest.apps.photo_manager.forms import *
from fotochest.apps.photo_manager.models import Photo, Album
from fotochest.apps.photo_manager.forms import AlbumForm


class Dashboard(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    """ Main dashboard view for the admin page.
    """
    paginate_by = 16
    template_name = "administrator/dashboard.html"
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.active()

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(parent_album=None)
        context['total_photos'] = Photo.objects.filter(deleted=False).count()
        context['total_albums'] = Album.objects.all().count()
        context['total_locations'] = Location.objects.all().count()
        return context

@login_required
@never_cache
def album_list(request):
    albums = Album.objects.parent_albums()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid:
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            messages.add_message(request, messages.SUCCESS, "Album %s created" % album.title)
            return redirect("admin_albums")
    else:
        form = AlbumForm()
    context = {'albums':albums, 'album_form':form}
    return render(request, "administrator/albums.html", context)

@login_required
@never_cache
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {}
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            messages.success(request, "Album %s saved." % album.title)
            return redirect("admin_albums")
    else:
        form = AlbumForm(instance=album)

    context['album_form'] = form
    context['album'] = album
    return render(request, "administrator/album_detail.html", context)

@login_required
@never_cache
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
@never_cache
def locations(request):
    context = {}
    context['locations'] = Location.objects.all()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_locations")
    else:
        form = LocationForm()
    context['form'] = form
    return render(request, "administrator/locations.html", context)


def choose(request):
    return redirect('file_uploader', location_slug=request.GET.get('location'), album_slug=request.GET.get("album"), user_id=request.GET.get('user_id'))

@login_required
@never_cache
def edit_photo(request, photo_id):
    context = {}
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo %s saved" % photo.title)
            return redirect('admin_dashboard')

    else:
        messages.error(request, "ERROR")
        return redirect('admin_dashboard')

@login_required
@never_cache
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id, deleted=False)
    photo.deleted = True
    photo.save()
    #@todo - This needs to point somewhere else after deletion..
    messages.success(request, "Photo %s deleted" % photo.title)
    return redirect('admin_dashboard')
    

@login_required
@never_cache
def rotate(request, photo_id, right=True):
    photo = Photo.objects.get(pk=photo_id)
    photo.rotate(right)
    return redirect('admin_dashboard')


class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'administrator/users.html'