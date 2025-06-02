from django.db import migrations, models
import django.db.models.deletion



# 000X_finalize_pk_and_cleanup.py
class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0005_migrate_connectionpoint_to_observable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionpoint',
            name='observablemodel_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstractModels.observablemodel'),
        ),
    ]
