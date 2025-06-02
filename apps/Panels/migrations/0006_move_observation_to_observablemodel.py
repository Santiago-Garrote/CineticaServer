from django.db import migrations

def move_observation_to_observablemodel(apps, schema_editor):
    Panel = apps.get_model('Panels', 'Panel')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    for panel in Panel.objects.all():
        observable = ObservableModel.objects.get(pk=panel.pk)
        observable.observations = panel.observation  # panel has 'observation', ObservableModel has 'observations'
        observable.save()

def reverse_func(apps, schema_editor):
    # Optional: move data back if needed
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('Panels', '0005_alter_panel_measurement'),
        ('abstractModels', '0006_finalize_pk_and_cleanup'),
        ('abstractModels', '0005_migrate_connectionpoint_to_observable'),
    ]

    operations = [
        migrations.RunPython(move_observation_to_observablemodel, reverse_func),
    ]
