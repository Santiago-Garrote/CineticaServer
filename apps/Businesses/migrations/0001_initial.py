# Generated by Django 5.1.7 on 2025-03-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cp', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('direction', models.CharField(max_length=50)),
                ('soil', models.CharField(max_length=50)),
            ],
        ),
    ]
