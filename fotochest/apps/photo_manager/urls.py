"""
fotochest.apps.photo_manager.urls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.conf.urls import url

from fotochest.apps.photo_manager import views, feeds


urlpatterns = [
    # Public URLS
    url(r'^$', views.HomepageListView.as_view(), name="homepage"),
    url(r'^photos/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/$', views.PhotoDetailView.as_view(), name="regular_photo_url"),
    url(r'^photos/(?P<album_slug>[-\w]+)/(?P<photo_slug>[-\w]+)/fullscreen/$', views.PhotoFullScreen.as_view(), name="photo_fullscreen"),

    # ShortURL
    url(r'^f/(?P<photo_id>\d+)/$', views.PhotoDetailView.as_view(), name="short_photo_url"),

    #download
    url(r'^photos/download/(?P<photo_id>\d+)/$', views.photo_download, name="photo_download"),
    # Map - This is not ideal. Should we have a maps.urls?

    url(r'map/$', views.LocationsListView.as_view(), name="map"),
    url(r'map/(?P<location_slug>[-\w]+)/$', views.PhotoLocationsListView.as_view(), name="photo_location"),

    # Feeds
    url(r'^feed/$', feeds.StreamFeed(), name="homepage_feed"),
    url(r'^album/(?P<album_slug>[-\w]+)/feed/$', feeds.AlbumStream(), name="album_stream"),

    # Albums
    url(r'^albums/$', views.AlbumListView.as_view(), name="albums"),
    url(r'^album/(?P<album_slug>[-\w]+)/$', views.AlbumDetailView.as_view(), name='album_detail'),

]
