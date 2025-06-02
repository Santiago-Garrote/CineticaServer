# 0012_finalize_circuitbreaker.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('CircuitBreakers', '0010_circuitbreaker_observablemodel_ptr'),
        ('Outlets','0006_remove_outlet_observations')
    ]

    operations = [

        migrations.RemoveField(
            model_name='circuitbreaker',
            name='observations',
        )
    ]
