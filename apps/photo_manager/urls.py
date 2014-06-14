from django.conf.urls import patterns, include, url

from .views import HomepageListView, LocationsListView, \
     photo_download, AlbumDetailView, AlbumListView, \
    PhotoLocationsListView, PhotoFullScreen, PhotoDetailView
from .feeds import StreamFeed, AlbumStream


urlpatterns = patterns('',
    # Public URLS
    url(r'^$', HomepageListView.as_view(), name="homepage"),
    url(r'^photos/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/$', PhotoDetailView.as_view(), name="regular_photo_url"),
    url(r'^photos/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/fullscreen/$', PhotoFullScreen.as_view(), name="photo_fullscreen"),
    
    # ShortURL
    url(r'^f/(?P<photo_id>\d+)/$', PhotoDetailView.as_view(), name="short_photo_url"),
    
    #download
    url(r'^photos/download/(?P<photo_id>\d+)/$', photo_download, name="photo_download"),
    # Map - This is not ideal. Should we have a maps.urls?
    
    url(r'map/$', LocationsListView.as_view(), name="map"),
    url(r'map/(?P<location_slug>[-\w]+)/$', PhotoLocationsListView.as_view(), name="photo_location"),
    
    # Feeds
    url(r'^feed/$', StreamFeed(), name="homepage_feed"),
    url(r'^album/(?P<album_slug>[-\w]+)/feed/$', AlbumStream(), name="album_stream"),
    
    # Albums
    url(r'^albums/$', AlbumListView.as_view(), name="albums"),
    url(r'^album/(?P<album_slug>[-\w]+)/$', AlbumDetailView.as_view(), name='album_detail'),

)

