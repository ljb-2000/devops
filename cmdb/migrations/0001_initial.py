# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
                ('desc', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ipaddr', models.IPAddressField(verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('username', models.CharField(default=b'root', max_length=20, verbose_name=b'\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('login_type', models.CharField(default=b'key', max_length=10, verbose_name=b'\xe8\xae\xa4\xe8\xaf\x81\xe6\x96\xb9\xe5\xbc\x8f', choices=[(b'password', b'\xe5\xaf\x86\xe7\xa0\x81'), (b'key', b'\xe5\xaf\x86\xe9\x92\xa5')])),
                ('password', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81', blank=True)),
                ('group', models.ForeignKey(verbose_name=b'\xe7\xbb\x84', to='cmdb.Group')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a',
                'verbose_name_plural': '\u4e3b\u673a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('contact', models.CharField(max_length=50, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba', blank=True)),
                ('tel', models.CharField(max_length=13, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('desc', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf', to='cmdb.IDC'),
            preserve_default=True,
        ),
    ]
