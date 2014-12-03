"""
fotochest.apps.administrator.views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


import json


from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings as app_settings
from django.core.urlresolvers import reverse
from django.core import management

from locations.models import Location
from locations.forms import LocationForm

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from fotochest.apps.photo_manager.forms import AlbumForm, PhotoForm
from fotochest.apps.photo_manager.models import Photo, Album
from fotochest.apps.administrator.utils import convert_bytes, get_size, get_randomized_file_name
from fotochest.apps.administrator.tasks import thumbnail_task


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


@never_cache
def get_cache_size(request):
    """ Get the size of the cache and return in ASYNC """
    size = convert_bytes(get_size(start_path='%s/cache' % app_settings.MEDIA_ROOT))
    return HttpResponse(size, content_type="text/plain")

@never_cache
def get_disk_size(request):
    """ Return the size of the photos on disk. ASYNC """
    size = convert_bytes(get_size())
    return HttpResponse(size, content_type="text/plain")


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

        thumbnail_task.delay(photo_new)

        # JQuery upload requires that you respond with JSON
        # Somethign like this..
        result = []
        result.append({"name": filename,
                       "size": file_size,
                       "url": "%s%s" % (app_settings.MEDIA_URL, photo_new.image),

                       "delete_url": reverse('upload_delete', args=[photo_new.pk]),
                       "delete_type": "POST"})
        response_data = json.dumps(result)

        #checking for json data type
        #big thanks to Guy Shapiro
        if "application/json" in request.META['HTTP_ACCEPT_ENCODING']:
            mimetype = 'application/json'
        else:
            mimetype = 'text/plain'
        return HttpResponse(response_data, content_type=mimetype)

    else:

        context['album_slug'] = album_slug
        context['location_slug'] = location_slug

        return render(request, 'administrator/add_photos.html', context)


def upload_delete(request, pk):
    return render(request, "example.html")


@login_required
@never_cache
def build_thumbnails(request):

    for photo in Photo.objects.all():
        photo.clear_thumbnails()
        photo.generate_thumbnails()
    messages.success(request, 'Job Queued.')

    return redirect('admin_utilities')

@login_required
def delete_thumbnails(request):
    for photo in Photo.objects.all():
        photo.clear_thumbnails()
    messages.success(request, "Thumbs deleted.")
    return redirect('admin_utilities')

@login_required
def clear_thumbnails(request):
    management.call_command('thumbnail', 'clear')
    messages.success(request, "Key Value Store Cleared")
    return redirect('admin_utilities')

@login_required
def rebuild_search(request):
    management.call_command('update_index')
    messages.success(request, "Search index updated.")
    return redirect('admin_utilities')