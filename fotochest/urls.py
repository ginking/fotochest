from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings


# This maps static files dirs to URLS.
urlpatterns = patterns('',

    # Admin URLS.
    url(r'^django_admin/', include(admin.site.urls)),
    url(r'^admin/', include("administrator.urls")),
    url(r'^search/', include('haystack.urls')),


    # Auth Views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'administrator/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^comments/', include('django.contrib.comments.urls')),
    #API Docs
    url(r'^docs/', include('api_docs.urls')),

    # Send all remaming URLS to the App.
    url(r'^', include('photo_manager.urls')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('',
        # Media URLs.
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': './uploads'}),
        url(r'^500/$', 'django.views.defaults.server_error'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
    )

    urlpatterns += staticfiles_urlpatterns()