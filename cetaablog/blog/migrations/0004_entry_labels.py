# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='labels',
            field=models.CharField(default=datetime.datetime(2015, 2, 5, 17, 5, 34, 694163, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
