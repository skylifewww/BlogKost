# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151010_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.ManyToManyField(to='article.Author', blank=True, verbose_name='Автор статьи', related_name='articles'),
        ),
    ]
