# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
    ]
