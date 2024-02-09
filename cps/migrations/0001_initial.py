# Generated by Django 5.0.1 on 2024-01-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinishGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Referencia', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('Stock', models.FloatField(blank=True)),
                ('Necesidad', models.IntegerField(blank=True)),
                ('Url', models.CharField(max_length=2083)),
            ],
        ),
    ]
