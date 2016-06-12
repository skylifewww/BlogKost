from django.conf.urls import url
import article.views
from django.conf.urls.static import static
from blogKost import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^videos/get/(?P<category_id>\d+)/(?P<article_id>\d+)/$', article.views.article),
    url(r'^page/article/addlike/(?P<article_id>\d+)/$', article.views.addlike),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
    url(r'^videos/page/$', article.views.articles),
    # url(r'^videos/page/(\d+)/$', article.views.articles),
    url(r'^article/page/(?P<art_page_number>\d+)/(?P<category_id>\d+)/$', article.views.article_left_right),
    url(r'^writtens/page/$', article.views.articles),
    # url(r'^writtens/page/(\d+)/$', article.views.articles),
    url(r'^$', article.views.articles),
    url(r'^category/get/(?P<category_id>\d+)/$', article.views.category),
    url(r'^author/get/(?P<author_id>\d+)/$', article.views.authors),
    url(r'^tag/get/(?P<tag_id>\d+)/$', article.views.tags),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)