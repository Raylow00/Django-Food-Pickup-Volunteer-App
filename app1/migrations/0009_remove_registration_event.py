# Generated by Django 2.2.4 on 2019-09-01 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_event_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
    ]