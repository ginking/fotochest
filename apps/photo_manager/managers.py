from django.db.models.query import QuerySet
from django.db.models import Manager


class PhotoQuerySet(QuerySet):
    def active(self):
        return self.filter(deleted=False)

    def public(self):
        return self.filter(private=False, deleted=False)

    def private(self):
        return self.filter(private=True, deleted=False)


class PhotoManager(Manager):

    def get_query_set(self):
        return PhotoQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()

    def public(self):
        return self.get_query_set().public()

    def private(self):
        return self.get_query_set().private()
