from django.conf.urls import include, url
from django.contrib import admin
from blogKost.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include("article.urls")),
    url(r'^auth/', include("loginsys.urls")),
    url(r'^$', slider),
    url(r'^tutorials/', tutorials),
    url(r'^contact/', contact),
    url(r'^portfolio/', portfolio),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^social/', include('social_auth.urls')),
]
