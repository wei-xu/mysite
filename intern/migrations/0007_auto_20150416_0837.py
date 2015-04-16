# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0006_auto_20150416_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 8, 37, 15, 983843), verbose_name=b'date published'),
        ),
    ]
