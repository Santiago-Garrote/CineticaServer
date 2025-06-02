from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Outlets', '0005_move_observations_to_observablemodel'),  # <-- new dependency
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlet',
            name='observations',
        ),
    ]
