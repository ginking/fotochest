from django.db.models.query import QuerySet
from django.db.models import Manager


class PhotoQuerySet(QuerySet):
    def active(self):
        return self.filter(deleted=False)


class PhotoManager(Manager):

    def get_query_set(self):
        return PhotoQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()


class AlbumQuerySet(QuerySet):
    def parent_albums(self):
        return self.filter(parent_album=None)


class AlbumManager(Manager):
    def get_query_set(self):
        return AlbumQuerySet(self.model, using=self._db)

    def parent_albums(self):
        return self.get_query_set().parent_albums()