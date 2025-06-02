from django.db import migrations

def migrate_and_rename_id(apps, schema_editor):
    ConnectionPoint = apps.get_model('abstractModels', 'ConnectionPoint')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    cursor = schema_editor.connection.cursor()



    # 1) Insertar ObservableModel con mismos ids que ConnectionPoint
    for cp in ConnectionPoint.objects.all():
        # Obtener ContentType específico de la instancia (usando for_concrete_model=False para obtener subclase real)
        ct = ContentType.objects.get_for_model(cp, for_concrete_model=False)

        cursor.execute(
            "INSERT INTO abstractModels_observablemodel (id, observations, polymorphic_ctype_id) VALUES (%s, '', %s)",
            [cp.id, ct.id]
        )

    # 2) Deshabilitar restricciones FK para renombrar columna
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

    # 3) Renombrar columna `id` a `observablemodel_ptr_id`
    cursor.execute("ALTER TABLE abstractModels_connectionpoint CHANGE COLUMN id observablemodel_ptr_id bigint NOT NULL;")

    # 4) Establecer `observablemodel_ptr_id` como PK
    cursor.execute("ALTER TABLE abstractModels_connectionpoint ADD PRIMARY KEY (observablemodel_ptr_id);")

    # 5) Crear FK hacia ObservableModel.id
    cursor.execute("""
        ALTER TABLE abstractModels_connectionpoint
        ADD CONSTRAINT connectionpoint_observablemodel_fk FOREIGN KEY (observablemodel_ptr_id)
        REFERENCES abstractModels_observablemodel(id) ON DELETE CASCADE;
    """)


    # 6) Ajustar constraints FK en esas tablas para apuntar a nueva PK
    # Connectors_connector.startConnectionPoint_id
    cursor.execute(
        "ALTER TABLE Connectors_connector DROP FOREIGN KEY Connectors_connector_startConnectionPoint_8ae0b9ed_fk_abstractM;")
    cursor.execute("""
                   ALTER TABLE Connectors_connector
                       ADD CONSTRAINT Connectors_connector_startConnectionPoint_8ae0b9ed_fk_abstractM
                           FOREIGN KEY (startConnectionPoint_id)
                               REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id) ON DELETE CASCADE;
                   """)

    # Connectors_connector.endConnectionPoint_id
    cursor.execute(
        "ALTER TABLE Connectors_connector DROP FOREIGN KEY Connectors_connector_endConnectionPoint_i_307527fd_fk_abstractM;")
    cursor.execute("""
                   ALTER TABLE Connectors_connector
                       ADD CONSTRAINT Connectors_connector_endConnectionPoint_i_307527fd_fk_abstractM
                           FOREIGN KEY (endConnectionPoint_id)
                               REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id) ON DELETE CASCADE;
                   """)

    # Javelins_javelin.connectionpoint_ptr_id
    cursor.execute(
        "ALTER TABLE Javelins_javelin DROP FOREIGN KEY Javelins_javelin_connectionpoint_ptr__2aa29503_fk_abstractM;")
    cursor.execute("""
                   ALTER TABLE Javelins_javelin
                       ADD CONSTRAINT Javelins_javelin_connectionpoint_ptr__2aa29503_fk_abstractM
                           FOREIGN KEY (connectionpoint_ptr_id)
                               REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id) ON DELETE CASCADE;
                   """)

    # Outlets_outlet.connectionpoint_ptr_id
    cursor.execute(
        "ALTER TABLE Outlets_outlet DROP FOREIGN KEY Outlets_outlet_connectionpoint_ptr__e7a3fdae_fk_abstractM;")
    cursor.execute("""
                   ALTER TABLE Outlets_outlet
                       ADD CONSTRAINT Outlets_outlet_connectionpoint_ptr__e7a3fdae_fk_abstractM
                           FOREIGN KEY (connectionpoint_ptr_id)
                               REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id) ON DELETE CASCADE;
                   """)

    # Panels_panel.connectionpoint_ptr_id
    cursor.execute("ALTER TABLE Panels_panel DROP FOREIGN KEY Panels_panel_connectionpoint_ptr__4059500c_fk_abstractM;")
    cursor.execute("""
                   ALTER TABLE Panels_panel
                       ADD CONSTRAINT Panels_panel_connectionpoint_ptr__4059500c_fk_abstractM
                           FOREIGN KEY (connectionpoint_ptr_id)
                               REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id) ON DELETE CASCADE;
                   """)

    # Reactivar restricciones FK
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")


def reverse_func(apps, schema_editor):
    # Implementar reverse si hace falta (complicado, opcional)
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0004_create_observablemodel_and_fk'),
    ]

    operations = [
        migrations.RunPython(migrate_and_rename_id, reverse_func),
    ]
