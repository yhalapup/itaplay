# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='administrator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.AdviserUser'),
        ),
    ]
