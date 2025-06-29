# Generated by Django 5.1.3 on 2025-06-02 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Businesses', '0001_initial'),
        ('Measurements', '0001_initial'),
        ('abstractModels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('connectionpoint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstractModels.connectionpoint')),
                ('hasBar', models.BooleanField()),
                ('section', models.FloatField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Businesses.business')),
                ('measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Measurements.patmeasurement')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('abstractModels.connectionpoint',),
        ),
        migrations.CreateModel(
            name='PrincipalPanel',
            fields=[
                ('panel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Panels.panel')),
                ('hasProtectors', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Panels.panel',),
        ),
        migrations.CreateModel(
            name='SectionalPanel',
            fields=[
                ('panel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Panels.panel')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Panels.panel',),
        ),
    ]
