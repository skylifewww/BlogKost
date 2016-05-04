from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogKost.views import *


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include("article.urls")),
    url(r'^auth/', include("loginsys.urls")),
    url(r'^$', slider),
    url(r'^tutorials/', tutorials),
    url(r'^contact/', contact),
    url(r'^portfolio/', portfolio),

    url(r'^redactor/', include('redactor.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
