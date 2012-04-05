from django.conf.urls import patterns, include, url
from administrator.views import dashboard, album_list, locations, album_detail, add_photos, photo_upload, add_location

# This maps static files dirs to URLS.
urlpatterns = patterns('',

        
    # Send all remaming URLS to the App.
    url(r'^$', dashboard, name="admin_dashboard"),
    url(r'^albums/$', album_list, name="admin_albums"),
    url(r'^album/(?P<album_id>\d+)/$', album_detail, name="admin_album_detail"),
    url(r'^locations/$', locations, name="admin_locations"),
    url(r'^locations/add/$', add_location, name="admin_add_location"),
    url(r'^add/$', add_photos, name="admin_add_photos"),
    url(r'^upload/(?P<album_slug>[-\w]+)/(?P<location_slug>[-\w]+)/$', photo_upload, name="file_uploader"),
)

