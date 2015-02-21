"""
fotochest.apps.api.urls
~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from django.conf.urls import url, patterns

from fotochest.apps.api import views


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

photo_list = views.PhotoViewSet.as_view({
    'get': 'list',
})

photo_detail = views.PhotoViewSet.as_view({
    'get': 'retrieve',
})

album_list = views.AlbumViewSet.as_view({
    'get': 'list',
})

album_detail = views.AlbumViewSet.as_view({
    'get': 'retrieve',
})


@api_view(('GET',))
def api_root(request, format=None):

    photo_directory = {
        'photo-listing': reverse('api-photo-list', request=request, format=format),
        'album-listing': reverse('api-album-list', request=request, format=format)
    }

    api_directory = {'FotoChest APIs': photo_directory}

    return Response(api_directory)


urlpatterns = patterns('',
    url(r'^$', api_root),

    url(r'^photo/$', photo_list, name='api-photo-list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', photo_detail, name='api-photo-detail'),

    url(r'^album/$', album_list, name='api-album-list'),
    url(r'^album/(?P<pk>[0-9]+)/$', album_detail, name='api-album-detail'),

)