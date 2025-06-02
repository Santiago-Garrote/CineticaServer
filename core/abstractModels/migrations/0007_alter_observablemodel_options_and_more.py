from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstractModels', '0006_finalize_pk_and_cleanup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='observablemodel',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='connectionpoint',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='connectionpoint',
            name='id',
        ),
        migrations.AlterField(
            model_name='observablemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
