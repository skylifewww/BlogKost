# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160519_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=mptt.fields.TreeForeignKey(blank=True, default='', max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='article.Author', verbose_name='Автор статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_category',
            field=mptt.fields.TreeForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='article.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, unique=True, verbose_name='Автор статьи'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='', max_length=25, unique=True, verbose_name='Название категории транслитом'),
        ),
    ]
