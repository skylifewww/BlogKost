# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import easy_thumbnails.fields
import article.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('article_title', models.CharField(verbose_name='Название статьи', max_length=200)),
                ('article_date', models.DateTimeField(verbose_name='Дата публикации статьи')),
                ('article_likes', models.IntegerField(verbose_name='Лайки', default=0)),
                ('short_text_ru', ckeditor.fields.RichTextField(verbose_name='Короткое описание RU', blank=True)),
                ('short_text_en', ckeditor.fields.RichTextField(verbose_name='Короткое описание EN', blank=True)),
                ('video', models.CharField(verbose_name='Видео id в кратком описании', blank=True, max_length=250)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Изображение', blank=True, upload_to=article.models.make_upload_path)),
                ('full_text_ru', ckeditor.fields.RichTextField(verbose_name='Полное описание RU', blank=True)),
                ('full_text_en', ckeditor.fields.RichTextField(verbose_name='Полное описание EN', blank=True)),
                ('article_video', embed_video.fields.EmbedVideoField(help_text='описание видео', verbose_name='Видео')),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'verbose_name': 'Статья',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author_name', models.CharField(verbose_name='Автор статьи', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Авторы',
                'verbose_name': 'Автор',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category_name', models.CharField(verbose_name='Название категории транслитом', max_length=25)),
                ('category_title', models.CharField(verbose_name='Имя категории', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категорию',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comments_create', models.DateTimeField(null=True, verbose_name='Дата', auto_now_add=True)),
                ('comments_text', models.TextField(verbose_name='Добавте Ваш комментарий')),
                ('comments_article', models.ForeignKey(verbose_name='Статья', to='article.Article')),
                ('comments_user', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, default=True)),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'verbose_name': 'Комментарий',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag_name', models.CharField(verbose_name='Название тега транслитом', max_length=25)),
                ('tag_title', models.CharField(verbose_name='Имя тега', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'тег',
                'verbose_name': 'тега',
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.ManyToManyField(to='article.Author', verbose_name='Автор статьи', blank=True, related_name='articles', default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(verbose_name='Категории', to='article.Category', related_name='articles', default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(verbose_name='Теги', related_name='articles', to='article.Tag'),
        ),
    ]
