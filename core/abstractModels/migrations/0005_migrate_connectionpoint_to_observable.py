# 000X_migrate_connectionpoint_to_observable.py
from django.db import migrations

def migrate_to_observable_pk(apps, schema_editor):
    ConnectionPoint = apps.get_model('abstractModels', 'ConnectionPoint')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    cursor = schema_editor.connection.cursor()

    old_to_new = {}

    for cp in ConnectionPoint.objects.all():
        # Create ObservableModel
        om = ObservableModel.objects.create(observations='')

        # Save reference in ConnectionPoint
        cp.observablemodel_ptr_id = om.id
        cp.save()

        # Store the mapping
        old_to_new[cp.id] = om.id

    # Now update the primary keys (raw SQL is safest here)
    for old_id, new_id in old_to_new.items():
        # 1. Update all foreign keys in other tables first (Connector, Javelin, Outlet, Panel)
        cursor.execute(
            f"UPDATE Connectors_connector SET startConnectionPoint_id = {new_id} WHERE startConnectionPoint_id = {old_id}")
        cursor.execute(
            f"UPDATE Connectors_connector SET endConnectionPoint_id = {new_id} WHERE endConnectionPoint_id = {old_id}")
        cursor.execute(
            f"UPDATE Javelins_javelin SET connectionpoint_ptr_id = {new_id} WHERE connectionpoint_ptr_id = {old_id}")
        cursor.execute(
            f"UPDATE Outlets_outlet SET connectionpoint_ptr_id = {new_id} WHERE connectionpoint_ptr_id = {old_id}")
        cursor.execute(
            f"UPDATE Panels_panel SET connectionpoint_ptr_id = {new_id} WHERE connectionpoint_ptr_id = {old_id}")

        # 2. Then update the primary key in ConnectionPoint
        cursor.execute(f"UPDATE abstractModels_connectionpoint SET id = {new_id} WHERE id = {old_id}")


def reverse_func(apps, schema_editor):
    # Optional: Write reverse logic here
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0004_create_observablemodel_and_fk'),
    ]

    operations = [
        migrations.RunPython(migrate_to_observable_pk, reverse_func),
    ]
