# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('realname', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1')),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8a\xa0\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('sex', models.CharField(default=b'male', max_length=b'10', verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')])),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe7\x99\xbb\xe9\x99\x86\xe5\x90\x8e\xe5\x8f\xb0')),
                ('is_superuser', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe7\x94\xa8')),
                ('groups', models.ManyToManyField(related_query_name=b'user', related_name=b'user_set', verbose_name=b'\xe7\xbb\x84', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name=b'user', related_name=b'user_set', verbose_name=b'\xe6\x9d\x83\xe9\x99\x90', to='auth.Permission')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            bases=(models.Model,),
        ),
    ]
