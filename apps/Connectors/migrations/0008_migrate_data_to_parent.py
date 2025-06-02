# 0011_migrate_data_to_parent.py
from django.db import migrations

def migrate_connector_to_observablemodel(apps, schema_editor):
    Connector = apps.get_model('Connectors', 'Connector')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    for connector in Connector.objects.all():
        # Get ContentType for Connector model (non-concrete to support proxy or inherited models)
        ct = ContentType.objects.get_for_model(connector, for_concrete_model=False)

        # Create ObservableModel row for this CircuitBreaker
        observable = ObservableModel.objects.create(
            # copy the fields from cb to observable here, e.g.
            # if ObservableModel has 'created_at', 'updated_at' etc, set them here.
            # add other fields shared between CircuitBreaker and ObservableModel
            observations=connector.observations,  # Copy observations field here
            polymorphic_ctype_id=ct.id,
        )

        # Link CircuitBreaker to ObservableModel
        connector.observablemodel_ptr_id = observable.pk
        connector.save()

def reverse_func(apps, schema_editor):
    # Optionally, write code to reverse the data migration if necessary
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('Connectors', '0007_connector_observablemodel_ptr'),
        ('abstractModels', '0005_migrate_connectionpoint_to_observable'),
    ]

    operations = [
        migrations.RunPython(migrate_connector_to_observablemodel, reverse_func),
    ]
