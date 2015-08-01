# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=40, unique=True, null=True)),
                ('user_name', models.CharField(max_length=40, null=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_city', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['user_id'],
                'verbose_name': 'User MetaData',
                'verbose_name_plural': 'Users MetaData',
            },
        ),
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_id', models.CharField(max_length=40, unique=True, null=True)),
                ('video_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'User_Video MetaData',
                'verbose_name_plural': 'Users_Video MetaData',
            },
        ),
        migrations.CreateModel(
            name='WatchedVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.PositiveIntegerField(null=True)),
                ('user', models.ForeignKey(to='graph.User', to_field=b'user_id')),
                ('videoData', models.ForeignKey(to='graph.VideoData', to_field=b'video_id')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='videos_watched',
            field=models.ManyToManyField(to='graph.VideoData', through='graph.WatchedVideo'),
        ),
    ]
