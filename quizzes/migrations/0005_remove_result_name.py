# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_auto_20150930_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='name',
        ),
    ]
