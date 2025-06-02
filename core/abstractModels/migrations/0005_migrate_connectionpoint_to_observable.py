from django.db import migrations, models
import django.db.models.deletion

import hashlib

def short_fk_name(table_name, column_name):
    base = f"{table_name}_{column_name}_fk_cp"
    if len(base) <= 64:
        return base
    # Hash para evitar colisiones
    hash_suffix = hashlib.md5(base.encode()).hexdigest()[:8]
    return f"{table_name[:20]}_{column_name[:20]}_{hash_suffix}_fk"


def migrate_and_rename_id(apps, schema_editor):
    ConnectionPoint = apps.get_model('abstractModels', 'ConnectionPoint')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    cursor = schema_editor.connection.cursor()

    # 1) Insertar ObservableModel con mismos ids que ConnectionPoint
    for cp in ConnectionPoint.objects.all():
        ct = ContentType.objects.get_for_model(cp, for_concrete_model=False)
        cursor.execute(
            "INSERT INTO abstractModels_observablemodel (id, observations, polymorphic_ctype_id) VALUES (%s, '', %s)",
            [cp.id, ct.id]
        )

    # 2) Deshabilitar FK temporalmente
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

    # 3) Obtener todas las FKs que apuntan a abstractModels_connectionpoint.id
    cursor.execute("""
        SELECT
            table_name,
            column_name,
            constraint_name
        FROM
            information_schema.key_column_usage
        WHERE
            referenced_table_schema = DATABASE()
            AND referenced_table_name = 'abstractModels_connectionpoint'
            AND referenced_column_name = 'id';
    """)
    fks = cursor.fetchall()

    # Guardar para luego recrearlas
    fk_info = []
    for table_name, column_name, constraint_name in fks:
        fk_info.append((table_name, column_name))
        cursor.execute(f'ALTER TABLE `{table_name}` DROP FOREIGN KEY `{constraint_name}`;')

    # 4) Renombrar columna y ajustar tipo
    cursor.execute("ALTER TABLE abstractModels_connectionpoint RENAME COLUMN id TO observablemodel_ptr_id;")
    cursor.execute("ALTER TABLE abstractModels_connectionpoint MODIFY COLUMN observablemodel_ptr_id bigint NOT NULL;")

    # 5) Cambiar PK
    cursor.execute("ALTER TABLE abstractModels_connectionpoint DROP PRIMARY KEY;")
    cursor.execute("ALTER TABLE abstractModels_connectionpoint ADD PRIMARY KEY (observablemodel_ptr_id);")

    # 6) Crear FK hacia abstractModels_observablemodel.id
    cursor.execute("""
        ALTER TABLE abstractModels_connectionpoint
        ADD CONSTRAINT connectionpoint_observablemodel_fk FOREIGN KEY (observablemodel_ptr_id)
        REFERENCES abstractModels_observablemodel(id) ON DELETE CASCADE;
    """)

    # 7) Recrear FKs originales dinámicamente
    for table_name, column_name in fk_info:
        constraint_name = short_fk_name(table_name, column_name)
        cursor.execute(f"""
            ALTER TABLE `{table_name}`
            ADD CONSTRAINT `{constraint_name}`
            FOREIGN KEY (`{column_name}`)
            REFERENCES abstractModels_connectionpoint (observablemodel_ptr_id)
            ON DELETE CASCADE;
        """)

    # 8) Reactivar FK
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")


def reverse_func(apps, schema_editor):
    # Omitido por ahora
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0004_create_observablemodel_and_fk'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(migrate_and_rename_id, reverse_func),
            ],
            state_operations=[
                migrations.RemoveField(
                    model_name='connectionpoint',
                    name='id',
                ),
                migrations.AddField(
                    model_name='connectionpoint',
                    name='observablemodel_ptr',
                    field=models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='abstractModels.observablemodel',
                    ),
                ),
            ],
        )
    ]
