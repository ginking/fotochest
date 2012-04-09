from photo_manager.models import Photo
### Jobs

''' Consider this for removal do to celery '''
def run_thumb_job(request):
    photos = Photo.objects.active().filter(thumbs_created=False)[:3]
    for photo in photos:
        try:
            photo.make_thumbnails()
            photo.thumbs_created = True
            photo.save()
        except:
            photo.thumbs_created = False
            photo.save()
            return HttpResponse("Thumb Creation Failure", mimetype="text/plain")
        
    return HttpResponse("Thumbs Created", mimetype="text/plain")

