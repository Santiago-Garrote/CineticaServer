# Generated by Django 5.1.3 on 2025-03-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Javelins', '0003_remove_javelin_business_javelin_connection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='javelin',
            name='usoPat',
            field=models.CharField(default='ok', max_length=50),
            preserve_default=False,
        ),
    ]
