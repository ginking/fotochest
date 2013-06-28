from django.contrib import admin

from .models import *


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


