# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentimage',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentimage',
            name='physical_page_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentimage',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
