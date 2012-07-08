from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from django.conf import settings


# This maps static files dirs to URLS.
urlpatterns = staticfiles_urlpatterns() + patterns('',

    # Admin URLS.
    url(r'^django_admin/', include(admin.site.urls)),
    url(r'^admin/', include("administrator.urls")),
    url(r'^search/', include('haystack.urls')),

    url(r'^500/$', 'django.views.defaults.server_error'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    # Auth Views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'administrator/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^comments/', include('django.contrib.comments.urls')),
    #API Docs
    url(r'^docs/', include('api_docs.urls')),

    # Media URLs.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': './uploads'}),

    # Send all remaming URLS to the App.
    url(r'^', include('photo_manager.urls')),
)

