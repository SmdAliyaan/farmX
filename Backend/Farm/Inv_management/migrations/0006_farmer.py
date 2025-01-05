

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv_management', '0005_alter_product_date_bought_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
