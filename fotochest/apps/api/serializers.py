from rest_framework import serializers


from fotochest.apps.photo_manager.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
