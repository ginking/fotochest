from django.http import HttpResponse
from django.conf import settings as app_settings
from django.views.decorators.cache import never_cache

from fotochest.utils.size import convert_bytes, get_size

@never_cache
def get_cache_size(request):
    """
    Get the size of the cache and return in ASYNC
    """
    size = convert_bytes(get_size(start_path = '%s/cache' % app_settings.MEDIA_ROOT))
    return HttpResponse(size, mimetype="text/plain")

@never_cache
def get_disk_size(request):
    """
    Return the size of the photos on disk. ASYNC
    """
    size = convert_bytes(get_size())
    return HttpResponse(size, mimetype="text/plain")



