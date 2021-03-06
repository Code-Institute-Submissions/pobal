# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('image', models.ImageField(blank=True, default='static/img/star.png', null=True, upload_to='img')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
