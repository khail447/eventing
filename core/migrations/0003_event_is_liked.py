# Generated by Django 3.2.6 on 2021-08-28 16:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_liked',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
