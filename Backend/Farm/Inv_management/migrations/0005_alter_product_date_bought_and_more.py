

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv_management', '0004_remove_product_quantity_product_date_bought_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_bought',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_expiration',
            field=models.DateField(blank=True, null=True),
        ),
    ]
