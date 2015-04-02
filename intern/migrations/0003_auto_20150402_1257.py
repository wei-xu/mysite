# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_auto_20150402_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
