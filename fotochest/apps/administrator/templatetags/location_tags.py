"""
fotochest.apps.administrator.templatetags.location_tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django import template
from fotochest.apps.photo_manager.models import Photo

register = template.Library()


@register.inclusion_tag('administrator/templatetags/locations.html')
def location_photo_count(location_slug):
    location_count = Photo.objects.filter(location__slug=location_slug).count()

    return {'location_count': location_count}
