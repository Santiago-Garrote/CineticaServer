from django.db import migrations

def migrate_to_observable_pk(apps, schema_editor):
    ConnectionPoint = apps.get_model('abstractModels', 'ConnectionPoint')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    cursor = schema_editor.connection.cursor()

    # Mapping from old ConnectionPoint.id to new ObservableModel.id
    old_to_new = {}

    for cp in ConnectionPoint.objects.all():
        # Create ObservableModel
        om = ObservableModel.objects.create(observations='')

        # Assign the new ID (ObservableModel.id) as the observablemodel_ptr_id
        cp.observablemodel_ptr_id = om.id
        cp.save()

        old_to_new[cp.id] = om.id

    # Now update FK references to point to new observablemodel_ptr_id
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

    for old_id, new_id in old_to_new.items():
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
        cursor.execute(
            # Drop foreign key constraints on dependent tables:
            "ALTER TABLE Panels_panel DROP FOREIGN KEY Panels_panel_connectionpoint_ptr_id_fk;",
            "ALTER TABLE Connectors_connector DROP FOREIGN KEY Connectors_connector_startConnectionPoint_id_fk;",
            "ALTER TABLE Connectors_connector DROP FOREIGN KEY Connectors_connector_endConnectionPoint_id_fk;",
            "ALTER TABLE Javelins_javelin DROP FOREIGN KEY Javelins_javelin_connectionpoint_ptr_id_fk;",
            "ALTER TABLE Outlets_outlet DROP FOREIGN KEY Outlets_outlet_connectionpoint_ptr_id_fk;",

            # Drop the id column from ConnectionPoint
            "ALTER TABLE abstractModels_connectionpoint DROP COLUMN id;",

            # Alter observablemodel_ptr to primary key
            "ALTER TABLE abstractModels_connectionpoint MODIFY observablemodel_ptr_id bigint NOT NULL PRIMARY KEY;",

            # Recreate the foreign keys now pointing to observablemodel_ptr_id
            "ALTER TABLE Panels_panel ADD CONSTRAINT Panels_panel_connectionpoint_ptr_id_fk FOREIGN KEY (connectionpoint_ptr_id) REFERENCES abstractModels_connectionpoint(observablemodel_ptr_id) ON DELETE CASCADE;",
            "ALTER TABLE Connectors_connector ADD CONSTRAINT Connectors_connector_startConnectionPoint_id_fk FOREIGN KEY (startConnectionPoint_id) REFERENCES abstractModels_connectionpoint(observablemodel_ptr_id) ON DELETE CASCADE;",
            "ALTER TABLE Connectors_connector ADD CONSTRAINT Connectors_connector_endConnectionPoint_id_fk FOREIGN KEY (endConnectionPoint_id) REFERENCES abstractModels_connectionpoint(observablemodel_ptr_id) ON DELETE CASCADE;",
            "ALTER TABLE Javelins_javelin ADD CONSTRAINT Javelins_javelin_connectionpoint_ptr_id_fk FOREIGN KEY (connectionpoint_ptr_id) REFERENCES abstractModels_connectionpoint(observablemodel_ptr_id) ON DELETE CASCADE;",
            "ALTER TABLE Outlets_outlet ADD CONSTRAINT Outlets_outlet_connectionpoint_ptr_id_fk FOREIGN KEY (connectionpoint_ptr_id) REFERENCES abstractModels_connectionpoint(observablemodel_ptr_id) ON DELETE CASCADE;",
        )
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")


def reverse_func(apps, schema_editor):
    # Optional: Write reverse logic here if needed
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0004_create_observablemodel_and_fk'),
    ]

    operations = [
        migrations.RunPython(migrate_to_observable_pk, reverse_func),
    ]
