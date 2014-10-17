# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20141016_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='group',
        ),
        migrations.AddField(
            model_name='host',
            name='groups',
            field=models.ManyToManyField(related_name=b'hosts', verbose_name=b'\xe7\xbb\x84', to='cmdb.Group'),
            preserve_default=True,
        ),
    ]
