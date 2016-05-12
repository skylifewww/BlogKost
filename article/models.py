# -*- coding: utf-8 -*-  

from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
# from mptt.models import MPTTModel
import random
from blogKost import settings
from easy_thumbnails.fields import ThumbnailerImageField


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    c = filename.split(".")
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + "." + c[-1]
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25, verbose_name="Название категории транслитом")
    category_title = models.CharField(max_length=25, verbose_name="Имя категории", blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_title


# class Author(models.Model):
#     author_name = models.CharField(max_length=200, verbose_name="Автор статьи")
#     author_title = models.CharField(max_length=200, verbose_name="Автор статьи транслитом", null=True, blank=True)

#     class Meta:
#         db_table = "authors"
#         verbose_name = "Автор"
#         verbose_name_plural = "Авторы"

#     def __str__(self):
#         return self.author_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=25, verbose_name="Название тега транслитом")
    tag_title = models.CharField(max_length=25, verbose_name="Имя тега")

    class Meta:
        db_table = "tags"
        verbose_name = "тега"
        verbose_name_plural = "тег"

    def __str__(self):
        return self.tag_title


class Article(models.Model):
    article_title = models.CharField(max_length=200, verbose_name="Название статьи")
    article_date = models.DateTimeField(verbose_name="Дата публикации статьи")
    article_likes = models.IntegerField(default=0, verbose_name="Лайки")
    article_tag = models.ManyToManyField(Tag, related_name="articles", verbose_name=u"Теги")
    article_category = models.ForeignKey(Category, default=0, related_name="articles", verbose_name="Категории")
    article_author = models.CharField(Author, related_name="autor", max_length=200, verbose_name="Автор статьи", blank=True)
    short_text_ru = RichTextUploadingField(blank=True, verbose_name="Короткое описание RU")
    short_text_en = RichTextUploadingField(blank=True, verbose_name="Короткое описание EN")
    video = models.CharField(max_length=250, blank=True, verbose_name="Видео id в кратком описании")
    image = ThumbnailerImageField(upload_to=make_upload_path, blank=True, verbose_name="Изображение")
    full_text_ru = RichTextUploadingField(blank=True, verbose_name="Полное описание RU")
    full_text_en = RichTextUploadingField(blank=True, verbose_name="Полное описание EN")
    article_video = EmbedVideoField(verbose_name='Видео', blank=True, help_text='описание видео')

    class Meta:
        db_table = 'article'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.article_title


# class Video(models.Model):
#     title = models.CharField(max_length=50)
#     video = EmbedVideoField(verbose_name='Видео',
#                             help_text='описание видео')
#     video_article = models.ForeignKey(Article, verbose_name="Статья")
#
#     class Meta:  # метка в базе данных
#         db_table = 'video'
#         verbose_name = "Видео"
#         verbose_name_plural = "Видео"
#
#     def __unicode__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('posts:detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    comments_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата", null=True, blank=True)
    comments_text = models.TextField(verbose_name="Добавте Ваш комментарий")
    comments_article = models.ForeignKey(Article, verbose_name="Статья")
    comments_user = models.ForeignKey(User, default=True, verbose_name="Пользователь")

    class Meta:
        db_table = 'comments'
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
