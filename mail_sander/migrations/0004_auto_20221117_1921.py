# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-17 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mail_sander", "0003_auto_20221117_1920"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailtemplate",
            name="template",
            field=models.CharField(max_length=100),
        ),
    ]
