# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        ('member', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='favorite_genre',
            field=models.ManyToManyField(blank=True, to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='favorite_grade',
            field=models.ManyToManyField(blank=True, to='movie.Grade'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='favorite_making_country',
            field=models.ManyToManyField(blank=True, to='movie.MakingCountry'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]