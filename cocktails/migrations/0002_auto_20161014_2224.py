# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cocktails',
            new_name='Cocktail',
        ),
    ]