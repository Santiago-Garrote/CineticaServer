# 0011_migrate_data_to_parent.py
from django.db import migrations

def migrate_circuitbreaker_to_observablemodel(apps, schema_editor):
    CircuitBreaker = apps.get_model('CircuitBreakers', 'CircuitBreaker')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    for cb in CircuitBreaker.objects.all():
        # Create ObservableModel row for this CircuitBreaker
        observable = ObservableModel.objects.create(
            # copy the fields from cb to observable here, e.g.
            # if ObservableModel has 'created_at', 'updated_at' etc, set them here.
            # add other fields shared between CircuitBreaker and ObservableModel
            observations=cb.observations,  # Copy observations field here
        )

        # Link CircuitBreaker to ObservableModel
        cb.observablemodel_ptr_id = observable.pk
        cb.save()

def reverse_func(apps, schema_editor):
    # Optionally, write code to reverse the data migration if necessary
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('CircuitBreakers', '0010_circuitbreaker_observablemodel_ptr'),
        ('abstractModels', '0005_migrate_connectionpoint_to_observable'),
    ]

    operations = [
        migrations.RunPython(migrate_circuitbreaker_to_observablemodel, reverse_func),
    ]
