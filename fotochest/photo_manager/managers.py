from django.db.models import Manager

class PhotoManager(Manager):
    def active(self):
        return self.model.objects.filter(deleted=False)
        