from django.conf import settings

from hadrian.contrib.locations.models import *

from .models import *
from defaults import VERSION_NUMBER

def locations_albums(request):
    context ={}
    context['form_locations'] = Location.objects.all()
    context['form_albums'] = Album.objects.all()
    return context
    
def version(request):
    context = {}
    context['version'] = VERSION_NUMBER
    context['app_name'] = settings.APP_NAME
    return context