# Generated by Django 2.0 on 2020-10-12 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20201012_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brendcategory',
        ),
        migrations.AddField(
            model_name='item',
            name='brendcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.BrendCategory'),
        ),
    ]
