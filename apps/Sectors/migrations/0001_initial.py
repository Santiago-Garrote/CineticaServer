# Generated by Django 5.1.3 on 2025-06-02 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Businesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('scheme', models.TextField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Businesses.business')),
            ],
        ),
    ]
