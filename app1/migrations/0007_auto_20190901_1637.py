# Generated by Django 2.2.4 on 2019-09-01 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20190901_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='start_date',
            new_name='date',
        ),
    ]
