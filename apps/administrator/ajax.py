from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from photo_manager.models import Photo, Album

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
