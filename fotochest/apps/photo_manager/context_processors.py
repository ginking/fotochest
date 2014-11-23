from django.conf import settings

from locations.models import Location

from fotochest.apps.photo_manager.models import Album


def locations_albums(request):
    context ={}
    context['form_locations'] = Location.objects.all()
    context['form_albums'] = Album.objects.all()
    return context


def version(request):
    context = {}
    context['version'] = 'Change Me'
    context['app_name'] = settings.APP_NAME
    return context