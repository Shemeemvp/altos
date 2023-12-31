# Generated by Django 4.2.3 on 2023-08-24 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_manufacture_date', models.DateField()),
                ('product_image', models.ImageField(upload_to='image/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.categoriesmodel')),
            ],
        ),
    ]
