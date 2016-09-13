from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogKost.views import *
from django.conf.urls.static import static
from blogKost import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include("article.urls")),
    url(r'^auth/', include("loginsys.urls")),
    url(r'^$', main),
    # url(r'^tutorials/', tutorials),
    url(r'^contact/', contact),
    # url(r'^portfolio/', portfolio),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    

    # url(r'', include('social.apps.django_app.urls', namespace='social'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
