"""
fotochest.apps.administrator.context_processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from fotochest.apps.photo_manager.models import Photo


def admin_context(request):
    context = {'thumbnails_building': Photo.objects.filter(deleted=False, thumbs_created=False).count()}

    return context