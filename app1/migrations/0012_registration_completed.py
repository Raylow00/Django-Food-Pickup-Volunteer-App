# Generated by Django 2.2.4 on 2019-09-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_event_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]