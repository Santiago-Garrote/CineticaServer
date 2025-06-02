from django.db import migrations, models
import django.db.models.deletion
import hashlib

def short_fk_name(table_name, column_name):
    base = f"{table_name}_{column_name}_fk_cb"
    if len(base) <= 64:
        return base
    hash_suffix = hashlib.md5(base.encode()).hexdigest()[:8]
    return f"{table_name[:20]}_{column_name[:20]}_{hash_suffix}_fk"


def migrate_and_rename_id(apps, schema_editor):
    CircuitBreaker = apps.get_model('CircuitBreakers', 'CircuitBreaker')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    cursor = schema_editor.connection.cursor()

    # 1) Crear nuevo ObservableModel por cada CB y mapear IDs
    id_map = {}
    for cb in CircuitBreaker.objects.all():
        ct = ContentType.objects.get_for_model(cb, for_concrete_model=False)
        cursor.execute(
            "INSERT INTO abstractModels_observablemodel (observations, polymorphic_ctype_id) VALUES (%s, %s)",
            [cb.observations, ct.id]
        )
        cursor.execute("SELECT LAST_INSERT_ID();")
        new_id = cursor.fetchone()[0]
        id_map[cb.id] = new_id

    # 2) Desactivar FK checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

    # 3) Detectar todas las FKs que apuntan a circuitbreakers_circuitbreaker.id
    cursor.execute("""
        SELECT
            table_name,
            column_name,
            constraint_name
        FROM
            information_schema.key_column_usage
        WHERE
            referenced_table_schema = DATABASE()
            AND referenced_table_name = 'CircuitBreakers_circuitbreaker'
            AND referenced_column_name = 'id';
    """)
    fks = cursor.fetchall()

    # 4) Eliminar esas FKs y guardar info para recrearlas
    fk_info = []
    for table_name, column_name, constraint_name in fks:
        fk_info.append((table_name, column_name))
        cursor.execute(f'ALTER TABLE `{table_name}` DROP FOREIGN KEY `{constraint_name}`;')

    # 5) Update CircuitBreaker rows and FKs that point to them
    for old_id, new_id in id_map.items():
        # Update CB ID
        cursor.execute(
            "UPDATE CircuitBreakers_circuitbreaker SET id = %s WHERE id = %s",
            [new_id, old_id]
        )

        # Update all FKs in related tables
        for table_name, column_name in fk_info:
            cursor.execute(
                f"UPDATE `{table_name}` SET `{column_name}` = %s WHERE `{column_name}` = %s",
                [new_id, old_id]
            )

    # 6) Renombrar y ajustar columna
    cursor.execute("ALTER TABLE CircuitBreakers_circuitbreaker RENAME COLUMN id TO observablemodel_ptr_id;")
    cursor.execute("ALTER TABLE CircuitBreakers_circuitbreaker MODIFY COLUMN observablemodel_ptr_id bigint NOT NULL;")

    # 7) Cambiar PK
    cursor.execute("ALTER TABLE CircuitBreakers_circuitbreaker DROP PRIMARY KEY;")
    cursor.execute("ALTER TABLE CircuitBreakers_circuitbreaker ADD PRIMARY KEY (observablemodel_ptr_id);")

    # 8) Agregar FK hacia abstractModels_observablemodel
    cursor.execute("""
        ALTER TABLE CircuitBreakers_circuitbreaker
        ADD CONSTRAINT circuitbreaker_observablemodel_fk FOREIGN KEY (observablemodel_ptr_id)
        REFERENCES abstractModels_observablemodel(id) ON DELETE CASCADE;
    """)

    # 9) Recrear FKs originales
    for table_name, column_name in fk_info:
        constraint_name = short_fk_name(table_name, column_name)
        cursor.execute(f"""
            ALTER TABLE `{table_name}`
            ADD CONSTRAINT `{constraint_name}`
            FOREIGN KEY (`{column_name}`)
            REFERENCES CircuitBreakers_circuitbreaker (observablemodel_ptr_id)
            ON DELETE CASCADE;
        """)

    # 10) Reactivar FK checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")


def reverse_func(apps, schema_editor):
    # Por simplicidad, omitido
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('CircuitBreakers', '0009_alter_circuitbreaker_options_and_more'),
        ('abstractModels', '0005_migrate_connectionpoint_to_observable'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(migrate_and_rename_id, reverse_func),
            ],
            state_operations=[
                migrations.RemoveField(
                    model_name='circuitbreaker',
                    name='id',
                ),
                migrations.AddField(
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
                ),
            ],
        ),
    ]
