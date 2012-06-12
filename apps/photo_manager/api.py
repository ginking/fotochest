from tastypie.resources import ModelResource
from photo_manager.models import Photo, Album
from hadrian.contrib.locations.models import Location
from tastypie import fields
from sorl.thumbnail import get_thumbnail


class AlbumResource(ModelResource):
    class Meta:
        queryset = Album.objects.all()
        resource = 'album'
        allowed_methods=['get']
        excludes = ['album_cover']
        
    def dehydrate(self, bundle):
        album_cover = bundle.obj.get_album_cover()
        cover_image_thumb = get_thumbnail(album_cover.image, "240x165")
        cover_image_large = get_thumbnail(album_cover.image, "1024x768")
        bundle.data['cover_image_thumb'] = cover_image_thumb.url
        bundle.data['cover_image_large'] = cover_image_large.url
        return bundle 

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get']


class PhotoResource(ModelResource):
    album = fields.ForeignKey(AlbumResource, 'album')
    location = fields.ForeignKey(LocationResource, 'location')
    
    class Meta:
        queryset = Photo.objects.all()
        resource_name = 'photo'
        include_absolute_url = True
        excludes = ['thumbs_created', 'file_name']
        
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(PhotoResource, self).build_filters(filters)
        if "album_id" in filters:
            orm_filters['album__id'] = filters['album_id']
        if "location_id" in filters:
            orm_filters['location__id'] = filters['location_id']
        return orm_filters
        
    def dehydrate(self, bundle):
        thumb_obj = get_thumbnail(bundle.obj.image, "240x165")
        thumb_square = get_thumbnail(bundle.obj.image, "75x75", crop="center")
        thumb_large = get_thumbnail(bundle.obj.image, "1024x768")
        bundle.data['short_url'] = "/f/%s/" % bundle.obj.id 
        bundle.data['thumb'] = thumb_obj.url
        bundle.data['thumb_square'] = thumb_square.url
        bundle.data['thumb_large'] = thumb_large.url
        bundle.data['location'] = bundle.obj.location.__unicode__()
        return bundle
        