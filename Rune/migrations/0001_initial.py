# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookingRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('subcategory', models.CharField(max_length=250)),
                ('skilllvl', models.IntegerField(blank=True, null=True)),
                ('sellvalue', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('sellvalue', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cookingrecipe',
            name='ingredient',
            field=models.ForeignKey(to='Rune.Ingredient'),
        ),
    ]
