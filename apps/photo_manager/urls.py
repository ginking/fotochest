from django.conf.urls import patterns, include, url
from photo_manager.views import homepage, photo, photo_fullscreen, locations, location, slideshow, album, albums, photo_download
from photo_manager.feeds import StreamFeed, AlbumStream
from django.conf import settings
from photo_manager.api import PhotoResource, UserResource, AlbumResource, LocationResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PhotoResource())
v1_api.register(AlbumResource())
v1_api.register(LocationResource())



urlpatterns = patterns('',
                       
    # Jobs
        
    url(r'^api/docs/', include('api_docs.urls')),
    url(r'^api/', include(v1_api.urls)),
                       
    # Public URLS
    url(r'^$', homepage, name="homepage"),    
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/$', photo, name="regular_photo_url"),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/fullscreen/$', photo_fullscreen),
    
    # ShortURL
    url(r'^f/(?P<photo_id>\d+)/$', photo, name="short_photo_url"),
    
    #download
    url(r'^foto/download/(?P<photo_id>\d+)/$', photo_download, name="photo_download"),
    # Map - This is not ideal. Should we have a maps.urls?
    
    url(r'map/$', locations, name="map"),
    url(r'map/(?P<location_slug>[-\w]+)/$', location),
    url(r'map/(?P<location_slug>[-\w]+)/slideshow/$', slideshow),
    
    # Feeds
    url(r'^feed/$', StreamFeed(), name="homepage_feed"),
    url(r'^album/(?P<album_slug>[-\w]+)/feed/$', AlbumStream(), name="album_stream"),
    
    # Albums
    url(r'^albums/$', albums, name="albums"),
    url(r'^album/(?P<album_id>\d+)/(?P<album_slug>[-\w]+)/$', album),
    url(r'^album/(?P<album_slug>[-\w]+)/slideshow/$', slideshow),                           
)

