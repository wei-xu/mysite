# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_auto_20150415_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 8, 35, 34, 597801), verbose_name=b'date published'),
        ),
    ]
