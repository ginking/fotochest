from django import forms
from photo_manager.models import Album
from administrator.models import Settings


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('user', 'album_cover',)
        
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings