from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from photo_manager.models import Photo, Album
from django.conf import settings as app_settings
import os

def update_photo_title(request):
    if request.method == "POST":
        photo_title = request.POST.get("photo_title")
        photo_id = request.POST.get("photo_id")
        photo = get_object_or_404(Photo, pk=photo_id)
        photo.title = photo_title
        photo.save()
        
    return HttpResponse("ok", mimetype="text/plain")
    

def update_album_title(request):
    if request.method == "POST":
        album_title = request.POST.get("album_title")
        album_id = request.POST.get("album_id")
        album = get_object_or_404(Album, pk=album_id)
        album.title = album_title
        album.save()
    
    return HttpResponse("ok", mimetype="text/plain")

def get_cache_size(request):
    size = convert_bytes(get_size(start_path = '%s/cache' % app_settings.MEDIA_ROOT))
    return HttpResponse(size, mimetype="text/plain")
    
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

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size