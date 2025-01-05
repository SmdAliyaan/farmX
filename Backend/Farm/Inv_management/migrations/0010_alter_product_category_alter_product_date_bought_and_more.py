

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Inv_management",
            "0009_remove_product_farmer_alter_product_date_bought_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Inv_management.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_bought",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_expiration",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity_remaining",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity_total",
            field=models.IntegerField(default=0),
        ),
    ]
