# Generated by Django 2.0 on 2020-10-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_partnyor'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='partnyor_title',
            field=models.CharField(blank=True, default='Partnyorlar', max_length=255, null=True),
        ),
    ]