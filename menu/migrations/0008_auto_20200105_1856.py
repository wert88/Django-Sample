# Generated by Django 3.0 on 2020-01-05 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20200105_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]