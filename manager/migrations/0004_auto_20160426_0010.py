# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20160425_2003'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestModel',
            new_name='TestModule',
        ),
        migrations.RenameField(
            model_name='testmodule',
            old_name='model_desc',
            new_name='module_desc',
        ),
        migrations.RenameField(
            model_name='testmodule',
            old_name='model_name',
            new_name='module_name',
        ),
    ]
