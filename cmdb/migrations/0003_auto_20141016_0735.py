# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20140924_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='host',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba'),
        ),
    ]
