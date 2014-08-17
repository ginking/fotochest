from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# This maps static files dirs to URLS.
urlpatterns = patterns('',

    # Admin URLS.
    url(r'^admin/', include("administrator.urls")),
    url(r'^django_admin/', include(admin.site.urls)),
    #url(r'^search/', include('haystack.urls')),

    # Auth Views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'administrator/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Send all remaming URLS to the App.
    url(r'^', include('photo_manager.urls')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += patterns('',

        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        url(r'^500/$', 'django.views.defaults.server_error'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),

    )
    urlpatterns += staticfiles_urlpatterns()