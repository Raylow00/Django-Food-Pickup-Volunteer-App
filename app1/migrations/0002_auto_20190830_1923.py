# Generated by Django 2.2.4 on 2019-08-30 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]