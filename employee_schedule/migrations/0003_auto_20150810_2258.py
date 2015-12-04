# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_schedule', '0002_timeslot_is_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end',
            field=models.TimeField(verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start',
            field=models.TimeField(verbose_name='start'),
        ),
    ]
