# Generated by Django 2.0.1 on 2019-10-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=25)),
                ('date_car', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_house', models.CharField(max_length=25)),
                ('date_house', models.DateField()),
            ],
        ),
    ]
