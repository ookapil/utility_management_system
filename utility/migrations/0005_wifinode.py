# Generated by Django 2.1.7 on 2019-03-25 16:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_wificable'),
    ]

    operations = [
        migrations.CreateModel(
            name='wifiNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router_poi', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]