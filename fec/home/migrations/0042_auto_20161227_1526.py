# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20161227_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutlandingpage',
            old_name='org_intro',
            new_name='leadership_intro',
        ),
    ]
