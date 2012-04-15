from administrator.models import Settings
from django.shortcuts import get_object_or_404

def settings(request):
    settings = get_object_or_404(Settings, pk=1)
    context = {'app_name':settings.app_name}
    return context    
    