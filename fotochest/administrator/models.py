from django.db import models

class Settings(models.Model):
    app_name = models.CharField(max_length=250, default="FotoChest", blank=True, null=True)
    enable_download = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return "Application Settings"
    