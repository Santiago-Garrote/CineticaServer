from django.db import migrations

def move_observations_to_observablemodel(apps, schema_editor):
    Javelin = apps.get_model('Javelins', 'Javelin')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    for javelin in Javelin.objects.all():
        observable = ObservableModel.objects.get(pk=javelin.pk)
        observable.observations = javelin.observations
        observable.save()

def reverse_func(apps, schema_editor):
    # Optional: reverse migration code if needed
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('Javelins', '0006_alter_javelin_connection_alter_javelin_status_and_more'),
        ('abstractModels', '0006_finalize_pk_and_cleanup'),
    ]

    operations = [
        migrations.RunPython(move_observations_to_observablemodel, reverse_func),
    ]
