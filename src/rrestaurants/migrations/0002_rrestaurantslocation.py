# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-25 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrestaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RRestaurantsLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_field001', models.DateTimeField()),
            ],
        ),
    ]