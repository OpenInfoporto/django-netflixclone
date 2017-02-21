# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Titolo')),
                ('story', models.TextField(null=True, verbose_name='Trama')),
                ('episode_number', models.IntegerField(verbose_name='Numero episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Nome stagione')),
                ('season_number', models.IntegerField(null=True, verbose_name='Numero stagione')),
            ],
        ),
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Titolo')),
                ('story', models.TextField(null=True, verbose_name='Trama')),
                ('cover_image', models.ImageField(null=True, upload_to=b'', verbose_name='Copertina')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='tvshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.TVShow'),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.Season'),
        ),
        migrations.AddField(
            model_name='episode',
            name='tvshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.TVShow'),
        ),
    ]