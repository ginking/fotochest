from fotochest.administrator.models import Settings
from fotochest.photo_manager.models import Photo
from django.shortcuts import get_object_or_404

def settings(request):
    settings = get_object_or_404(Settings, pk=1)
    context = {'app_name':settings.app_name, 'enable_download':settings.enable_download}
    context['thumbnails_building'] = Photo.objects.filter(deleted=False, thumbs_created=False).count()
    return context