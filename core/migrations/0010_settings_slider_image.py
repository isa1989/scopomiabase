# Generated by Django 2.0 on 2020-09-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200926_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='slider_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
