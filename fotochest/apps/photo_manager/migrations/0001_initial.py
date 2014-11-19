# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('parent_album', models.ForeignKey(blank=True, to='photo_manager.Album', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, blank=True)),
                ('file_name', models.CharField(max_length=400, editable=False)),
                ('image', models.ImageField(max_length=400, upload_to=b'images/')),
                ('description', models.TextField(null=True, blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('thumbs_created', models.BooleanField(default=False, editable=False)),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('album', models.ForeignKey(to='photo_manager.Album')),
                ('location', models.ForeignKey(blank=True, to='locations.Location', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
    ]
