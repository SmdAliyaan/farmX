

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Inv_management", "0007_product_farmer"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
