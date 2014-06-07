import os

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from utils.slugs import unique_slugify
from locations.models import *

from sorl.thumbnail import get_thumbnail, delete

from PIL import Image
from PIL.ExifTags import TAGS

from .managers import PhotoManager
from .tasks import clear_thumbnails, build_thumbnails


class Album(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True, auto_now_add=True)
    parent_album = models.ForeignKey('self', blank=True, null=True)
    album_cover = models.ImageField(upload_to="cover_art/", max_length=400, blank=True, null=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Album, self).save(*args, **kwargs)
        
    def _get_preview_photos(self):
        """ Private method to return the first five photos
        in this album
        """

        return Photo.objects.filter(album=self)[:5]
        
    def _get_album_cover(self):
        """ Fetch the photo to be used for the album cover
        for this album.  Attempt to loop through the children
        of the album to find an acceptable candidate photo.
        """

        this_photo = ""
        try:
            photos = Photo.objects.filter(album=self)[:1].get()
            return photos
        except:
            # Try for first Child.
            try:
                album = Album.objects.filter(parent_album=self)[:1].get()
                photos = Photo.objects.filter(album=album)[:1].get()
                return photos
                    
            except:
                # one final layer down
                try:
                    album = Album.objects.filter(parent_album=self)[:1].get()
                    use_album = Album.objects.filter(parent_album=album)[:1].get()
                    photos = Photo.objects.filter(album=use_album)[:1].get()
                    return photos
                except:
                    pass
                    this_photo = ""
        return this_photo

    @property
    def album_cover(self):
        return self._get_album_cover()

    @property
    def preview_photos(self):
        """ Returns first 5 photos from the album
        to be used in preview for album.
        """

        return self._get_preview_photos()

    @property
    def has_child_albums(self):
        """ Returns true if this album has child albums.
        """
        return Album.objects.filter(parent_album=self).count()

    @property
    def count(self):
        """ Return the count of photos in this album.
        """
        return Photo.objects.filter(album=self).count()

    @models.permalink
    def get_absolute_url(self):
        """ @todo - Add Comments
        """
        return ('album_detail', (), {'album_slug': self.slug})

    @models.permalink
    def get_admin_url(self):
        """ @todo - Add Comments
        """
        return ('administrator.views.album_detail', (), {'album_id':self.id})


class Photo(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False, blank=True)
    file_name = models.CharField(max_length=400, editable=False)
    image = models.ImageField(upload_to="images/", max_length=400)
    description = models.TextField(null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now=False, auto_now_add=True)
    album = models.ForeignKey(Album)
    user = models.ForeignKey(User, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    thumbs_created = models.BooleanField(default=False, editable=False)
    deleted = models.BooleanField(default=False, editable=False)
    
    objects = PhotoManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Photo, self).save()

    @property
    def author(self):
        """ Return a text string of the author
        of this photo.  If a user has a first and last use that,
        otherwise use the username.
        """
        if self.user.first_name and self.user.last_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        return self.user.username
    
    @property    
    def filename(self):
        """ @todo - Add Comments
        """
        return os.path.basename(self.image.name)
    
    @models.permalink
    def get_next(self):
        """ @todo - Add Comments
        """
        try:
            next_photo = Photo.objects.filter(id__lt=self.id, user=self.user)[:1]
            photo = next_photo[0]
        except:
            return None
        return ('regular_photo_url', (), {'photo_slug': photo.slug, 'album_slug': photo.album.slug})
    
    @models.permalink
    def get_previous(self):
        """ @todo - Add Comments
        """
        try:
            prev_photo = Photo.objects.filter(id__gt=self.id, user=self.user).order_by('id')[:1]
            photo = prev_photo[0]
        except:
            return None
        return ('regular_photo_url', (), {'photo_slug': photo.slug, 'album_slug': photo.album.slug})
        
    def image_preview(self):
        """ @todo - Add Comments
        """
        im = get_thumbnail(self.image, "150x150")
        return '<img src="%s" width="150"/>'  % im.url
    image_preview.allow_tags = True

    def _clear_thumbnails(self):
        """ Actual code to clear the thumbnails.  Private.
        """

        delete(self.image, delete_file=False)
        self.thumbs_created = False
        self.save()

    def clear_thumbnails(self):
        """ Remove any and all thumbnails for this photo
        from the disk and DB.  Useful when making photo changes
        or when something funky happens to the thumbnails.

        Public API.

        """

        clear_thumbnails.apply_async(args=[self], countdown=10)

    def generate_thumbnails(self, force=False):
        """ Model method to generate thumbnails for
        images used on the site.  Determines if the site
        will use Celery to Queue it up or not.  If the user does not
        have Celery enabled we will only make thumbnails on the template
        when they are desired.

        Public API.

        """

        build_thumbnails.apply_async(args=[self], countdown=10)

    def make_thumbnails(self):
        """ Generate thumbnail sizes that
        are used throughout the site.  When a new size is used
        add it here so that it can be generated on upload.
        """
        get_thumbnail(self.image, '75x75', crop="center", quality=50)
        get_thumbnail(self.image, '1024x650', quality=100)
        get_thumbnail(self.image, '240x165')
        get_thumbnail(self.image, '240x161', crop="center", quality=75)
        get_thumbnail(self.image, '300x220')
        get_thumbnail(self.image, '300x300')

        self.thumbs_created = True
        self.save()

    def rotate(self, right=True):
        """ @todo - Add Comments
        """
        path = "%s/%s" % (settings.MEDIA_ROOT, self.image)
        im = Image.open(path)
        if right:
            im.rotate(270).save(path)
        else:
            im.rotate(90).save(path)
        self.clear_thumbnails()
        self.generate_thumbnails()

    def get_exif_data(self):
        """ @todo - Add Comments
        """
        exif_data = {}
        i = Image.open(self.image)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
        return exif_data

    #@todo - point to new class ivew.
    @models.permalink
    def get_absolute_url(self):
        """ @todo - Add Comments
        """
        return ('regular_photo_url', (), {'photo_slug': self.slug, 'album_slug': self.album.slug})
    
    @models.permalink
    def get_fullscreen(self):
        """ @todo - Add Comments
        """
        # update with enable multi user
        return ('photo_fullscreen', (), {'photo_slug': self.slug, 'album_slug': self.album.slug})

    class Meta:
        ordering = ['-id']


def photos_by_location(location):
    """ @todo - Add Comments
        """
    return Photo.objects.filter(deleted=False, location=location).count()
