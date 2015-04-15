# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0003_auto_20150402_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='belonging',
            field=models.CharField(default=b'Pe', max_length=20, choices=[(b'Pe', b'Personal'), (b'Pu', b'Public')]),
            preserve_default=True,
        ),
    ]
