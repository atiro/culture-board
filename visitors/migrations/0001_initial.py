# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('visitors', models.IntegerField()),
                ('organisation', models.ForeignKey(to='common.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='Monthly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('visitors', models.IntegerField()),
                ('organisation', models.ForeignKey(to='common.Organisation')),
            ],
        ),
    ]
