# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20151011_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_title',
            field=models.CharField(verbose_name='Автор статьи транслитом', blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(verbose_name='Имя категории', blank=True, max_length=25, default=True),
        ),
    ]
