# Generated by Django 5.1.3 on 2025-03-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Panels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='observation',
            field=models.CharField(max_length=100),
        ),
    ]
