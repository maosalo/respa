# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-27 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0066_support_for_django_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='reservation_requested_notification_extra',
            field=models.TextField(
                blank=True,
                verbose_name=(
                    'Extra content to "reservation requested" notification')),
        ),
    ]
