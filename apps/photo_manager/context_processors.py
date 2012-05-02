from locations.models import *
from django.conf import settings

def theme_files(request):
    context = {}
    
    context['THEME_URL'] = "%sphoto_manager/themes/%s/" % (settings.STATIC_URL, settings.ACTIVE_THEME)
    
    return context
   