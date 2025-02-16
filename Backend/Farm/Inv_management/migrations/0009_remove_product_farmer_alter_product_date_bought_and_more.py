

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Inv_management", "0008_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="farmer",
        ),
        migrations.AlterField(
            model_name="product",
            name="date_bought",
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="date_expiration",
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=datetime.date.today, upload_to="product_images/"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
