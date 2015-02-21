from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# This maps static files dirs to URLS.
urlpatterns = patterns('',

    # Admin URLS.
    url(r'^admin/', include("fotochest.apps.administrator.urls")),
    url(r'^support/', include(admin.site.urls)),

    # Auth Views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'administrator/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Send all remaming URLS to the App.
    url(r'^', include('fotochest.apps.photo_manager.urls')),
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