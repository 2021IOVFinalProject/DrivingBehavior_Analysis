# Generated by Django 2.1.15 on 2021-08-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='dateTimeOfUpload',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
