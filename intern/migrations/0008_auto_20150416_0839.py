# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0007_auto_20150416_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
