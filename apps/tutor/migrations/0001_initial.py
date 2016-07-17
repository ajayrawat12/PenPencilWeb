# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=50, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Others', b'Others')])),
                ('joining_date', models.DateTimeField(default=datetime.datetime(2016, 7, 16, 8, 17, 28, 987000, tzinfo=utc))),
                ('T_user', models.OneToOneField(verbose_name=b'related to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='TutorInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prof_pic', models.ImageField(null=True, upload_to=b'profile_pic', blank=True)),
                ('full_name', models.TextField(max_length=30)),
                ('exp', models.PositiveSmallIntegerField()),
                ('age', models.PositiveSmallIntegerField()),
                ('courses', models.TextField(max_length=500)),
                ('T_link', models.OneToOneField(verbose_name=b'of Tutor user', to='tutor.Tutor')),
            ],
        ),
    ]
