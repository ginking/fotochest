from django import forms
from photo_manager.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('user', 'album_cover',)