# Generated by Django 3.1.1 on 2020-11-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('logical_uid', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Listed'), (False, 'Unlisted')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='logging',
            fields=[
                ('logical_uid', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(max_length=144)),
                ('qty', models.IntegerField()),
                ('time', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=144, unique=True)),
                ('passwd', models.CharField(max_length=144)),
                ('permission', models.CharField(max_length=144)),
            ],
        ),
    ]
