# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='quiz_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='quiz_score',
            new_name='score',
        ),
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 19, 1, 23, 54456, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
