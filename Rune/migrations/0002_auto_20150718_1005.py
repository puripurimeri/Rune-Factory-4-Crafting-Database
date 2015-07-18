# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rune', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CookingRecipe',
            new_name='Recipe',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='sellvalue',
        ),
    ]
