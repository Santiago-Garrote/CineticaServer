from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Javelins', '0007_move_observations_to_observablemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='javelin',
            name='observations',
        ),
    ]
