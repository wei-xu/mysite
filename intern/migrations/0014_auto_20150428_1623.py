# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0013_wiki_wikiedithistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki',
            name='wiki_content',
            field=models.TextField(verbose_name=b'content'),
        ),
        migrations.AlterField(
            model_name='wiki',
            name='wiki_pagename',
            field=models.CharField(max_length=60, verbose_name=b'pagename'),
        ),
    ]
