from django.conf.urls import patterns, include, url
from fotochest.administrator.views.general import Dashboard, album_list, locations, album_detail, add_photos, add_location, choose, edit_photo,\
    delete_photo, rotate_photo, CommentListView,\
    delete_comment, rotate_right, rotate_left
from fotochest.administrator.views.edit import rotate
from fotochest.administrator.views.utils import build_thumbnails, delete_thumbnails, clear_thumbnails, rebuild_search
from fotochest.administrator.views.upload import upload_photo, upload_delete
from fotochest.administrator.views.ajax import get_disk_size, get_cache_size
# This maps static files dirs to URLS.
from django.views.generic import TemplateView
urlpatterns = patterns('',

        
    # Send all remaming URLS to the App.
    url(r'^$', Dashboard.as_view(), name="admin_dashboard"),
    url(r'^choose/', choose, name="choose"),
    url(r'^comments/$', CommentListView.as_view(), name="comment_list_view"),
    url(r'^comments/delete/(?P<comment_id>\d+)/$', delete_comment, name="comment_delete_view"),
    url(r'^albums/$', album_list, name="admin_albums"),
    url(r'^album/(?P<album_id>\d+)/$', album_detail, name="admin_album_detail"),
    url(r'^locations/$', locations, name="admin_locations"),
    url(r'^locations/add/$', add_location, name="admin_add_location"),

    url(r'^utilities/$', TemplateView.as_view(template_name='administrator/utilities.html'), name="admin_utilities"),
    url(r'^utilities/build/$', build_thumbnails, name="build_thumbnails"),
    url(r'^utilities/search/update/$', rebuild_search, name="rebuild_search"),
    url(r'^utilities/thumbs/delete/$', delete_thumbnails, name="delete_thumbnails"),
    url(r'^utilities/thumbs/clear/$', clear_thumbnails, name="clear_thumbnails"),
    
    url(r'^add/$', add_photos, name="admin_add_photos"),
    url(r'^foto/(?P<photo_id>\d+)/edit/$', edit_photo, name="admin_edit_photo"),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/delete/$', delete_photo),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/rotate/(?P<rotate_direction>[-\w]+)/$', rotate_photo),
    url(r'^upload/(?P<album_slug>[-\w]+)/(?P<location_slug>[-\w]+)/(?P<user_id>\d+)/$', upload_photo, name="file_uploader"),
    url(r'^upload/delete/(?P<pk>\d+)$', upload_delete, name='upload_delete'),

    url(r'^edit/(?P<photo_id>\d+)/rotate/right/$', rotate, name="admin_rotate_right"),
    url(r'^edit/(?P<photo_id>\d+)/rotate/left/$', rotate, {'right': True }, name="admin_rotate_left"),

    #ajaxy
    
    url(r'^ajax/disk/size/$', get_disk_size),
    url(r'^ajax/cache/size/$', get_cache_size),
)

