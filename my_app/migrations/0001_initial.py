# Generated by Django 5.1.2 on 2024-11-11 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveBigIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('status', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employees',
                'ordering': ['id'],
            },
        ),
    ]
