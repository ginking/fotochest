from celery.task import task


@task(name='fotochest.photo_manager.clear_thumbnails')
def clear_thumbnails(photo):
    """ @todo - Add Comments
        """

    photo._clear_thumbnails()

@task(name='fotochest.photo_manager.build_thumbnails')
def build_thumbnails(photo):
    """ @todo - Add Comments
        """
    photo.make_thumbnails()