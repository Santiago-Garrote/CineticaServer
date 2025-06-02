# 0012_finalize_circuitbreaker.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('CircuitBreakers', '0011_migrate_data_to_parent'),
        ('Outlets','0006_remove_outlet_observations')
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuitbreaker',
            name='id',
        ),
        migrations.RemoveField(
            model_name='circuitbreaker',
            name='observations',
        ),
        migrations.AlterField(
            model_name='circuitbreaker',
            name='observablemodel_ptr',
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to='abstractModels.observablemodel',
            ),
        )
    ]
