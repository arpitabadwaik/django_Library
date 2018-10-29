# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveRegistrationData',
            fields=[
                ('full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('e_mail', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('user_name', models.CharField(max_length=100, serialize=False, primary_key=True, blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
