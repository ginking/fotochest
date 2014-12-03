"""
fotochest.apps.photo_manager.context_processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.conf import settings

from locations.models import Location

from fotochest.apps.photo_manager.models import Album


def locations_albums(request):
    context = {'form_locations': Location.objects.all(), 'form_albums': Album.objects.all()}
    return context


def version(request):
    context = {'version': 'Change Me', 'app_name': settings.APP_NAME}
    return context