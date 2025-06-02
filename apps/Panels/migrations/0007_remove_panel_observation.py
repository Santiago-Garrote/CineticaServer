from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Panels', '0006_move_observation_to_observablemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='observation',
        ),
    ]
