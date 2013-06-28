from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# This maps static files dirs to URLS.
urlpatterns = patterns('',

    # Admin URLS.
    url(r'^admin/', include("fotochest.administrator.urls")),
    #url(r'^search/', include('haystack.urls')),

    # Auth Views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'administrator/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^comments/', include('django.contrib.comments.urls')),
    #API Docs
    url(r'^docs/', include('api_docs.urls')),

    # Send all remaming URLS to the App.
    url(r'^', include('fotochest.photo_manager.urls')),
)

