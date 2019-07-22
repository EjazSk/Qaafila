# Generated by Django 2.2.3 on 2019-07-21 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Qaafila', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='darja',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]