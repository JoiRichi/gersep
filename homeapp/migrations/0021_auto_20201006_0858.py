# Generated by Django 3.1 on 2020-10-06 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0020_auto_20201006_0850'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DownloadRate',
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 7, 58, 34, 105344, tzinfo=utc)),
        ),
    ]
