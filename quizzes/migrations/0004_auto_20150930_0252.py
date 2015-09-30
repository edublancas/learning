# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20150930_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='deck',
            field=models.ForeignKey(default=1, to='quizzes.Deck'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='deck',
            field=models.ForeignKey(default=1, to='quizzes.Deck'),
            preserve_default=False,
        ),
    ]
