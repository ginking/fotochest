from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

from .models import Album, Photo

class AlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Field('title', css_class='span4'),
            Field('description', css_class='span4'),
            Field('parent_album', css_class='span4'),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )
        
        super(AlbumForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Album
        exclude = ('user', 'album_cover',)
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo