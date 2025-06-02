from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('CircuitBreakers', '0009_alter_circuitbreaker_options_and_more'),
        ('abstractModels', '0006_finalize_pk_and_cleanup'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuitbreaker',
            name='observablemodel_ptr',
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=False,
                serialize=False,
                to='abstractModels.observablemodel',
            ),
        ),
    ]
