# Generated by Django 3.0 on 2020-01-05 16:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_album_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 16, 48, 39, 303759, tzinfo=utc)),
        ),
    ]
