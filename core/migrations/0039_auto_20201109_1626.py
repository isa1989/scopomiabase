# Generated by Django 2.0 on 2020-11-09 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20201029_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brendcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brend', to='core.BrendCategory'),
        ),
    ]
