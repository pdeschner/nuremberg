# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_documentevidencecode_documentevidenceprefix_documentexhibitcode_documentexhibitcodename'),
        ('transcripts', '0005_auto_20160619_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='activities',
            field=models.ManyToManyField(related_name='transcripts', to='documents.DocumentActivity'),
        ),
    ]
