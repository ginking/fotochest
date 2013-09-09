from django.core import management
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from photo_manager.models import Photo
from utils.celery import is_using_celery

__author__ = 'Derek Stegelman'
__date__ = '9/22/12'

@login_required
@never_cache
def build_thumbnails(request):
    if is_using_celery():
        for photo in Photo.objects.all():
            photo.clear_thumbnails()
            photo.generate_thumbnails()
        messages.success(request, 'Job Queued.')
    else:
        messages.error(request, 'You MUST enable celery to perform this Job.')
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