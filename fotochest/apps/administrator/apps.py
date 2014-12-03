"""
fotochest.apps.administrator.apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.apps import AppConfig


class AdminConfig(AppConfig):
    name = 'fotochest.apps.administrator'
    label = 'administrator'
    verbose_name = 'Admin'