# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('portfolio', '0003_auto_20160905_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'title', max_length=100)),
                ('link', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=100)),
                ('picture', models.ImageField(help_text=b'This picture needs to have square dimensions or it will render incorrectly.', upload_to=b'work/')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('work', models.ForeignKey(to='portfolio.Work')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
