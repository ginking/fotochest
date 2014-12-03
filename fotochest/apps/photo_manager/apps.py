"""
fotochest.apps.photo_manager.apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.apps import AppConfig


class PhotoConfig(AppConfig):
    name = 'fotochest.apps.photo_manager'
    label = 'photo_manager'
    verbose_name = 'Photos'