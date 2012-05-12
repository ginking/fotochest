from django import forms
from photo_manager.models import Album
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class AlbumForm(forms.ModelForm):

    

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='span4'),
            Field('description', css_class='span4'),
            Field('parent_album', css_class='span4'),
        )
        super(AlbumForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Album
        exclude = ('user', 'album_cover',)
        
