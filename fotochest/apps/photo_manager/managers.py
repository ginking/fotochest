from django.db.models.query import QuerySet


class PhotoQuerySet(QuerySet):
    def active(self):
        return self.filter(deleted=False)


class AlbumQuerySet(QuerySet):
    def parent_albums(self):
        return self.filter(parent_album=None)
