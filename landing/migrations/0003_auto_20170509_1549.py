# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_subscriber_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='message',
            new_name='comment',
        ),
    ]
