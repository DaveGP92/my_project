# Generated by Django 5.1.2 on 2024-11-14 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_type_employee_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='my_app.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('sell_date', models.DateTimeField(null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('customer', models.ForeignKey(db_column='cuetomer_id', on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='my_app.customer')),
            ],
            options={
                'verbose_name': 'sale',
                'verbose_name_plural': 'sales',
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='my_app.product')),
                ('sale', models.ForeignKey(db_column='sale_id', on_delete=django.db.models.deletion.CASCADE, related_name='sale_detail', to='my_app.sale')),
            ],
            options={
                'verbose_name': 'sale detail',
                'verbose_name_plural': 'sale details',
                'db_table': 'sale_details',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
