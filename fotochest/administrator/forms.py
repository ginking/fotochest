from django import forms
from administrator.models import Settings
        
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings