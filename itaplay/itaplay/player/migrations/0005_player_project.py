# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-05 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_adviserproject_player'),
        ('player', '0004_auto_20160823_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.AdviserProject'),
        ),
    ]