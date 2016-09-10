# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.AdviserProject'),
        ),
    ]
