# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('portfolio', '0002_auto_20160905_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='workpluginmodel',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='workpluginmodel',
            name='work',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.DeleteModel(
            name='WorkPluginModel',
        ),
    ]
