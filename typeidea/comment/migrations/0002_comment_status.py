# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-06 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '\u6b63\u5e38'), (2, '\u5220\u9664')], default=1, verbose_name='\u72b6\u6001'),
        ),
    ]
