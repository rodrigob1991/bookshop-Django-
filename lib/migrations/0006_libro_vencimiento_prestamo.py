# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0005_auto_20171004_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='vencimiento_prestamo',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
