# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-12 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20190212_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='hostgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.GroupHost', verbose_name='主机组'),
        ),
    ]