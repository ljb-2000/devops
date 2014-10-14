# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_key'),
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='port',
            field=models.CharField(default=b'22', max_length=10, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='private_key',
            field=models.ForeignKey(verbose_name=b'\xe5\xaf\x86\xe9\x92\xa5', blank=True, to='account.Key', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'\xe5\x8f\xaf\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba'),
            preserve_default=True,
        ),
    ]
