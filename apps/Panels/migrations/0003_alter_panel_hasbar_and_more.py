# Generated by Django 5.1.3 on 2025-03-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Panels', '0002_alter_panel_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='hasBar',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='principalpanel',
            name='hasProtectors',
            field=models.BooleanField(),
        ),
    ]
