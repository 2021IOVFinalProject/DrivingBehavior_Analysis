# Generated by Django 3.2.8 on 2021-11-12 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211010_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='Driver_Type',
            new_name='Average_EngineRPM',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='Average_speed',
            new_name='Average_Vehiclespeed',
        ),
        migrations.RemoveField(
            model_name='file',
            name='Engine_RPM',
        ),
        migrations.RemoveField(
            model_name='file',
            name='Vehicle_speed',
        ),
        migrations.AddField(
            model_name='file',
            name='Driver_Risk',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]