# Generated by Django 3.1 on 2020-08-25 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeapp', '0004_auto_20200825_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsfeed',
            old_name='published_date',
            new_name='deadline',
        ),
        migrations.RemoveField(
            model_name='newsfeed',
            name='created_date',
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='submit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='author',
            field=models.ForeignKey(blank=True, default='accounts.CustomUser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
