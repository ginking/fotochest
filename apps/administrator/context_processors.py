from fotochest.photo_manager.models import Photo

def settings(request):
    context = {}
    context['thumbnails_building'] = Photo.objects.filter(deleted=False, thumbs_created=False).count()
    return context