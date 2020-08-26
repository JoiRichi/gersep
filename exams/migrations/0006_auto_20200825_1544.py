# Generated by Django 3.1 on 2020-08-25 14:44

import accounts.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0005_auto_20200825_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_code', models.CharField(default='GER/EDO/AN/INT/00', max_length=200)),
                ('text', models.TextField(max_length=2000)),
                ('submit_date', models.DateTimeField(default=datetime.datetime(2020, 8, 25, 14, 44, 24, 551457, tzinfo=utc))),
                ('score', models.FloatField(default=0)),
                ('email', models.ForeignKey(blank=True, default=accounts.models.CustomUser, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]