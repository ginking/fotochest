from locations.models import *
from photo_manager.models import *
from django.conf import settings

def theme_files(request):
    context = {}
    
    context['ENABLE_REGISTRATION'] = settings.ENABLE_REGISTRATION
    context['THEME_URL'] = "%sphoto_manager/themes/%s/" % (settings.STATIC_URL, settings.ACTIVE_THEME)
    
    return context

def locations_albums(request):
    context = {}
    context['form_locations'] = Location.objects.all()
    context['form_albums'] = Album.objects.all()
    return context
    
    