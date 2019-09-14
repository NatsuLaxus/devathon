# Generated by Django 2.1.2 on 2019-09-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('vehicle_num', models.CharField(max_length=128)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('vehicle_num', models.CharField(max_length=128)),
                ('vehicle_type', models.IntegerField()),
            ],
        ),
    ]