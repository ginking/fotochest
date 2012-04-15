from django.conf.urls import patterns, include, url
from administrator.views import dashboard, album_list, locations, album_detail, add_photos, photo_upload, add_location, choose, edit_photo, delete_photo, rotate_photo, settings

# This maps static files dirs to URLS.
urlpatterns = patterns('',

        
    # Send all remaming URLS to the App.
    url(r'^$', dashboard, name="admin_dashboard"),
    url(r'^choose/', choose, name="choose"),
    url(r'^albums/$', album_list, name="admin_albums"),
    url(r'^album/(?P<album_id>\d+)/$', album_detail, name="admin_album_detail"),
    url(r'^locations/$', locations, name="admin_locations"),
    url(r'^locations/add/$', add_location, name="admin_add_location"),
    url(r'^settings/$', settings, name="settings"),
    url(r'^add/$', add_photos, name="admin_add_photos"),
    url(r'^update_photo_title/$', 'administrator.ajax.update_photo_title'),
    url(r'^update_album_title/$', 'administrator.ajax.update_album_title'),
    url(r'^thumb_job/$', 'administrator.jobs.run_thumb_job'),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/edit/$', edit_photo),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/delete/$', delete_photo),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/rotate/(?P<rotate_direction>[-\w]+)/$', rotate_photo),
    url(r'^upload/(?P<album_slug>[-\w]+)/(?P<location_slug>[-\w]+)/$', photo_upload, name="file_uploader"),
)

