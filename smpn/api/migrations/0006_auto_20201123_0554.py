# Generated by Django 3.1.1 on 2020-11-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_inventory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='logical_uid',
            field=models.CharField(default='GN-00', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]