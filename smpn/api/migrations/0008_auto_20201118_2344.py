# Generated by Django 3.1.1 on 2020-11-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201118_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logging',
            name='status',
            field=models.BooleanField(choices=[(True, 'Listed'), (False, 'Unlisted')], null=True),
        ),
    ]