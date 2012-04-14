# Add an inline to the admin Yo!

from django.db import models
from django.contrib.auth.models import User
from photo_manager.models import Photo
from django.db.models.signals import post_save
from profiles.choices import *

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    theme = models.CharField(max_length=250, choices=THEME_CHOICES)
    profile_picture = models.ImageField(upload_to="profile_pics/", max_length=400, blank=True, null=True)
    
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


