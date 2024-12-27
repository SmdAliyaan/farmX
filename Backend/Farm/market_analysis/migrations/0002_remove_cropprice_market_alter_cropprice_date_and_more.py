# Generated by Django 5.1.4 on 2024-12-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropprice',
            name='market',
        ),
        migrations.AlterField(
            model_name='cropprice',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cropprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]