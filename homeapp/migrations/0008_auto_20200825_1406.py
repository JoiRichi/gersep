# Generated by Django 3.1 on 2020-08-25 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_auto_20200825_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 13, 6, 40, 400797, tzinfo=utc)),
        ),
    ]
