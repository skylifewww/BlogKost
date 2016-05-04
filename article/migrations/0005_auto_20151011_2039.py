# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20151011_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_author',
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(blank=True, verbose_name='Автор статьи', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(blank=True, null=True, verbose_name='Имя категории', max_length=25),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
