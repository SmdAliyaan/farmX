

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv_management', '0006_farmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inv_management.farmer'),
        ),
    ]
