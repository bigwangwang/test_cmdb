# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-11 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.ManyToManyField(blank=True, to='cmdb.Disk', verbose_name='磁盘'),
        ),
    ]
