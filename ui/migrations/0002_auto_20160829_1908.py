# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='site',
            name='a',
        ),
        migrations.RemoveField(
            model_name='site',
            name='b',
        ),
        migrations.RemoveField(
            model_name='site',
            name='date',
        ),
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(default='Site name', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Site'),
        ),
    ]
