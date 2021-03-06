# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_adviseruser_id_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adviserinvitations',
            old_name='id_company',
            new_name='IdCompany',
        ),
        migrations.RenameField(
            model_name='adviserinvitations',
            old_name='is_active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='adviserinvitations',
            old_name='verification_code',
            new_name='verificationCode',
        ),
        migrations.RenameField(
            model_name='adviseruser',
            old_name='id_company',
            new_name='IdCompany',
        ),
        migrations.AddField(
            model_name='adviserinvitations',
            name='creationTime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 7, 11, 5, 41, 994967, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adviserinvitations',
            name='usedTime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 7, 11, 11, 35, 806108, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
