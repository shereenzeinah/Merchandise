# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaser', '0007_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='address',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
