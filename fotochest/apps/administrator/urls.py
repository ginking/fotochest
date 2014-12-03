"""
fotochest.apps.administrator.urls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from fotochest.apps.administrator import views


urlpatterns = patterns('',
    # Send all remaming URLS to the App.
    url(r'^$', views.Dashboard.as_view(), name="admin_dashboard"),
    url(r'^choose/', views.choose, name="choose"),
    url(r'^albums/$', views.album_list, name="admin_albums"),
    url(r'^album/(?P<album_id>\d+)/$', views.album_detail, name="admin_album_detail"),
    url(r'^locations/$', views.locations, name="admin_locations"),
    url(r'^locations/add/$', views.add_location, name="admin_add_location"),

    url(r'^utilities/$', TemplateView.as_view(template_name='administrator/utilities.html'), name="admin_utilities"),
    url(r'^utilities/build/$', views.build_thumbnails, name="build_thumbnails"),
    url(r'^utilities/search/update/$', views.rebuild_search, name="rebuild_search"),
    url(r'^utilities/thumbs/delete/$', views.delete_thumbnails, name="delete_thumbnails"),
    url(r'^utilities/thumbs/clear/$', views.clear_thumbnails, name="clear_thumbnails"),

    url(r'^users/$', views.UserList.as_view(), name='admin_user_list'),

    url(r'^add/$', login_required(TemplateView.as_view(template_name="administrator/add_photos.html")), name="admin_add_photos"),
    url(r'^foto/(?P<photo_id>\d+)/edit/$', views.edit_photo, name="admin_edit_photo"),
    url(r'^foto/(?P<photo_id>\d+)/delete/$', views.delete_photo, name='admin_photo_delete'),
    url(r'^upload/(?P<album_slug>[-\w]+)/(?P<location_slug>[-\w]+)/(?P<user_id>\d+)/$', views.upload_photo, name="file_uploader"),
    url(r'^upload/delete/(?P<pk>\d+)$', views.upload_delete, name='upload_delete'),

    url(r'^edit/(?P<photo_id>\d+)/rotate/right/$', views.rotate, name="admin_rotate_right"),
    url(r'^edit/(?P<photo_id>\d+)/rotate/left/$', views.rotate, {'right': True}, name="admin_rotate_left"),

    #ajaxy
    
    url(r'^ajax/disk/size/$', views.get_disk_size),
    url(r'^ajax/cache/size/$', views.get_cache_size),
)

