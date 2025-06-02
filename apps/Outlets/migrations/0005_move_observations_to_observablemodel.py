from django.db import migrations

def move_observations_to_observablemodel(apps, schema_editor):
    Outlet = apps.get_model('Outlets', 'Outlet')
    ObservableModel = apps.get_model('abstractModels', 'ObservableModel')

    for outlet in Outlet.objects.all():
        observable = ObservableModel.objects.get(pk=outlet.pk)
        observable.observations = outlet.observations
        observable.save()

def reverse_func(apps, schema_editor):
    # Optional: reverse the migration if needed
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('Outlets', '0004_alter_outlet_measurement'),
        ('abstractModels', '0006_finalize_pk_and_cleanup'),
    ]

    operations = [
        migrations.RunPython(move_observations_to_observablemodel, reverse_func),
    ]
