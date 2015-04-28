# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0012_auto_20150421_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wiki_pagename', models.CharField(max_length=60, verbose_name=b'title')),
                ('wiki_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WikiEditHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edit_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'edit time')),
                ('edit_reason', models.CharField(max_length=200, verbose_name=b'reason')),
                ('edit_pagename', models.ForeignKey(to='intern.Wiki')),
            ],
        ),
    ]
