from django.conf.urls import patterns, include, url

from django.contrib.auth.decorators import login_required

from .views.general import Dashboard, album_list, locations, album_detail, add_location, choose, edit_photo,\
    delete_photo, rotate, UserList
from administrator.views.utils import build_thumbnails, delete_thumbnails, clear_thumbnails, rebuild_search
from administrator.views.upload import upload_photo, upload_delete
from administrator.views.ajax import get_disk_size, get_cache_size
# This maps static files dirs to URLS.
from django.views.generic import TemplateView
urlpatterns = patterns('',

        
    # Send all remaming URLS to the App.
    url(r'^$', Dashboard.as_view(), name="admin_dashboard"),
    url(r'^choose/', choose, name="choose"),
    url(r'^albums/$', album_list, name="admin_albums"),
    url(r'^album/(?P<album_id>\d+)/$', album_detail, name="admin_album_detail"),
    url(r'^locations/$', locations, name="admin_locations"),
    url(r'^locations/add/$', add_location, name="admin_add_location"),

    url(r'^utilities/$', TemplateView.as_view(template_name='administrator/utilities.html'), name="admin_utilities"),
    url(r'^utilities/build/$', build_thumbnails, name="build_thumbnails"),
    url(r'^utilities/search/update/$', rebuild_search, name="rebuild_search"),
    url(r'^utilities/thumbs/delete/$', delete_thumbnails, name="delete_thumbnails"),
    url(r'^utilities/thumbs/clear/$', clear_thumbnails, name="clear_thumbnails"),

    url(r'^users/$', UserList.as_view(), name='admin_user_list'),

    url(r'^add/$', login_required(TemplateView.as_view(template_name="administrator/add_photos.html")), name="admin_add_photos"),
    url(r'^foto/(?P<photo_id>\d+)/edit/$', edit_photo, name="admin_edit_photo"),
    url(r'^foto/(?P<photo_id>\d+)/delete/$', delete_photo, name='admin_photo_delete'),
    url(r'^upload/(?P<album_slug>[-\w]+)/(?P<location_slug>[-\w]+)/(?P<user_id>\d+)/$', upload_photo, name="file_uploader"),
    url(r'^upload/delete/(?P<pk>\d+)$', upload_delete, name='upload_delete'),

    url(r'^edit/(?P<photo_id>\d+)/rotate/right/$', rotate, name="admin_rotate_right"),
    url(r'^edit/(?P<photo_id>\d+)/rotate/left/$', rotate, {'right': True}, name="admin_rotate_left"),

    #ajaxy
    
    url(r'^ajax/disk/size/$', get_disk_size),
    url(r'^ajax/cache/size/$', get_cache_size),
)

