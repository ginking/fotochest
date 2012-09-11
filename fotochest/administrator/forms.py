from django import forms
from fotochest.administrator.models import Settings
        
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings