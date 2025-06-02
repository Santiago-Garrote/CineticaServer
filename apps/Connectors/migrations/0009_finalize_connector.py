from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('Connectors', '0008_migrate_data_to_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connector',
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
        migrations.RemoveField(
            model_name='connector',
            name='id',
        ),
        migrations.RemoveField(
            model_name='connector',
            name='observations',
        ),
    ]
