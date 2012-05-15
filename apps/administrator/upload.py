from fileupload.models import Picture
from django.views.generic import CreateView, DeleteView

from django.http import HttpResponse
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'thumbnail_url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)
        
# Real Methods

def upload_photo(request, location_slug, album_slug, user_id):
    context = {}
    if request.method == 'POST':
        #
        uploaded_file = request.FILES[u'files[]']
        
        # write the file into /tmp
        num1 = str(random.randint(0, 1000000))
        num2 = str(random.randint(1001, 9000000))
        
        ext = os.path.splitext(uploaded_file.name)[1]
        filename = str(num1 + num2) + ext
        
        album_used = get_object_or_404(Album, slug=album_slug)
        photo_new = Photo(title=filename, album=album_used)
        photo_new.file_name = filename
        photo_new.image = 'images/' + filename
        # Set location to default location
        photo_new.location = get_object_or_404(Location, slug=location_slug)
        user = get_object_or_404(User, pk=user_id)
        photo_new.user = user
        photo_new.save()
            
        destination_path = app_settings.PHOTO_DIRECTORY + '/%s' % (filename)   
        destination = open(destination_path, 'wb+')
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
        destination.close()
        ENABLE_CELERY = getattr(app_settings, 'ENABLE_CELERY', defaults.ENABLE_CELERY)
        if ENABLE_CELERY:
            ThumbnailTask.delay(photo_new.id)

        
        return HttpResponse("ok", mimetype="text/plain")
        
    else:
        
        context['upload_dir'] = app_settings.PHOTO_DIRECTORY
        context['album_slug'] = album_slug
        context['location_slug'] = location_slug
        context['domain_static'] = app_settings.DOMAIN_STATIC    
        return render(request,'administrator/add_photos.html', context)