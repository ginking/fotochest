from django.core import management
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.conf import settings as app_settings
from django.contrib.auth.decorators import login_required

from fotochest.photo_manager.models import Photo
from fotochest.conf import defaults
from fotochest.administrator.tasks import thumbnail_cleanup_task, thumbnail_task

__author__ = 'Derek Stegelman'
__date__ = '9/22/12'

@login_required
@never_cache
def build_thumbnails(request):
    ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
    for photo in Photo.objects.all():
        photo.thumbs_created = False
        photo.save()
        if ENABLE_CELERY:
            thumbnail_task.delay(photo)
    messages.add_message(request, messages.SUCCESS, "Job queued.")
    return redirect('admin_utilities')

@login_required
def delete_thumbnails(request):
    for photo in Photo.objects.all():
        thumbnail_cleanup_task.delay(photo)
    messages.add_message(request, messages.SUCCESS, "Thumbs deleted.")
    return redirect('admin_utilities')

@login_required
def clear_thumbnails(request):
    management.call_command('thumbnail', 'clear')
    messages.add_message(request, messages.SUCCESS, "Key Value Store Cleared")
    return redirect('admin_utilities')

@login_required
def rebuild_search(request):
    management.call_command('update_index')
    messages.add_message(request, messages.SUCCESS, "Search index updated.")
    return redirect('admin_utilities')