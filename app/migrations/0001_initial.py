# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollno', models.IntegerField(default=100)),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
    ]
