"""
fotochest.apps.photo_manager.context_processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from django.conf import settings

from locations.models import Location

from fotochest.apps.photo_manager.models import Album
from fotochest import defaults


def photo_context(request):
    context = {'form_locations': Location.objects.all(), 'form_albums': Album.objects.all()}
    context["version"] = defaults.FOTOCHEST_VERSION
    context['app_name'] = settings.APP_NAME

    return context