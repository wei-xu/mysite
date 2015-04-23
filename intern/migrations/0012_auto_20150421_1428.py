# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0011_auto_20150417_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date uploaded'),
        ),
        migrations.AddField(
            model_name='document',
            name='uploader',
            field=models.CharField(default=b'undefined', max_length=40, verbose_name=b'uploader'),
        ),
    ]
