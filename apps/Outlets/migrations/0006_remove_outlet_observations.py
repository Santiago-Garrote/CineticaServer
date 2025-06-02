from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('Outlets', '0005_move_observations_to_observablemodel'),
        ('CircuitBreakers', '0010_circuitbreaker_observablemodel_ptr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlet',
            name='observations',
        ),
        migrations.AlterField(
            model_name='outlet',
            name='circuitBreaker',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='CircuitBreakers.circuitbreaker',
                to_field='observablemodel_ptr'
            ),
        ),
    ]
