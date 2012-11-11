import os

from django.http import HttpResponse
from django.conf import settings as app_settings
from django.views.decorators.cache import never_cache

from fotochest.utils.size import convert_bytes

@never_cache
def get_cache_size(request):
    size = convert_bytes(get_size(start_path = '%s/cache' % app_settings.MEDIA_ROOT))
    return HttpResponse(size, mimetype="text/plain")

@never_cache
def get_disk_size(request):
    size = convert_bytes(get_size())
    return HttpResponse(size, mimetype="text/plain")

def get_size(start_path = '%s/images' % app_settings.MEDIA_ROOT):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

