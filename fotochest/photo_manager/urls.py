from django.conf.urls import patterns, include, url

from fotochest.photo_manager.views import HomepageListView, LocationsListView, album, photo_download, AlbumListView, PhotoLocationsListView, PhotoFullScreen, PhotoDetailView
from fotochest.photo_manager.feeds import StreamFeed, AlbumStream
from fotochest.photo_manager.api import PhotoResource, AlbumResource, LocationResource

from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(PhotoResource())
v1_api.register(AlbumResource())
v1_api.register(LocationResource())

urlpatterns = patterns('',
        
    url(r'^api/docs/', include('api_docs.urls')),
    url(r'^api/', include(v1_api.urls)),
                       
    # Public URLS
    url(r'^$', HomepageListView.as_view(), name="homepage"),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/$', PhotoDetailView.as_view(), name="regular_photo_url"),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/fullscreen/$', PhotoFullScreen.as_view(), name="photo_fullscreen"),
    
    # ShortURL
    url(r'^f/(?P<photo_id>\d+)/$', photo, name="short_photo_url"),
    
    #download
    url(r'^foto/download/(?P<photo_id>\d+)/$', photo_download, name="photo_download"),
    # Map - This is not ideal. Should we have a maps.urls?
    
    url(r'map/$', LocationsListView.as_view(), name="map"),
    url(r'map/(?P<location_slug>[-\w]+)/$', PhotoLocationsListView.as_view(), name="photo_location"),
    
    # Feeds
    url(r'^feed/$', StreamFeed(), name="homepage_feed"),
    url(r'^album/(?P<album_slug>[-\w]+)/feed/$', AlbumStream(), name="album_stream"),
    
    # Albums
    url(r'^albums/$', AlbumListView.as_view(), name="albums"),
    url(r'^album/(?P<album_id>\d+)/(?P<album_slug>[-\w]+)/$', album),

)

