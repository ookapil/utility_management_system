# Generated by Django 2.1.7 on 2019-03-25 15:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0002_roadnetwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='waterPipeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.IntegerField()),
                ('meterial', models.CharField(max_length=50)),
                ('where_from', models.CharField(max_length=50)),
                ('towhere', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
    ]