from django.conf.urls import patterns, include, url
from photo_manager.views import *
from photo_manager.feeds import *
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
    url(r'^thumb_job/$', run_thumb_job),
    url(r'^update_photo_title/$', update_photo_title),
    url(r'^update_album_title/$', update_album_title),
    url(r'^api/docs/', include('api_docs.urls')),
    url(r'^api/', include(v1_api.urls)),
                       
    # Public URLS
    url(r'^$', homepage, name="homepage"),
        
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/$', photo, name="regular_photo_url"),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/fullscreen/$', photo_fullscreen),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/edit/$', edit_photo),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/delete/$', delete_photo),
    url(r'^foto/(?P<photo_id>\d+)/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/rotate/(?P<rotate_direction>[-\w]+)/$', rotate_photo),
    
    # ShortURL
    url(r'^f/(?P<photo_id>\d+)/$', photo, name="short_photo_url"),
    
    
    # Map - This is not ideal. Should we have a maps.urls?
    
    url(r'map/$', locations, name="map"),
    url(r'map/(?P<location_slug>[-\w]+)/$', location),
    url(r'map/(?P<location_slug>[-\w]+)/slideshow/$', slideshow),
    
    #url(r'map/user/(?P<username>[-\w]+)/$', locations),
    #url(r'map/user/(?P<username>[-\w]+)/(?P<location_slug>[-\w]+)/$', location),
    
    
    # Upload
    
    url(r'^choose/', choose, name="choose"),
    # Feeds
    url(r'^feed/$', StreamFeed(), name="homepage_feed"),
    url(r'^album/(?P<album_slug>[-\w]+)/feed/$', AlbumStream(), name="album_stream"),
    
    # Albums
    url(r'^albums/$', albums, name="albums"),
    url(r'^album/(?P<album_id>\d+)/(?P<album_slug>[-\w]+)/$', album),
    url(r'^album/(?P<album_slug>[-\w]+)/slideshow/$', slideshow),                           
)

