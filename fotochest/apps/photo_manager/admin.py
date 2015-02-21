"""
fotochest.apps.photo_manager.admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.contrib import admin

from fotochest.apps.photo_manager.models import Album, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'location', 'image_preview', 'thumbs_created')
    list_filter = ('album', 'location')
    list_per_page = 10
    search_fields = ('title', 'album__name', 'location')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_album', 'user', 'slug')
    search_fields = ('title', 'slug')
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)


