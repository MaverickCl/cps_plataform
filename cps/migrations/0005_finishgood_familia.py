# Generated by Django 5.0.1 on 2024-02-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cps', '0004_remove_bom_id_remove_finishgood_stock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishgood',
            name='Familia',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
