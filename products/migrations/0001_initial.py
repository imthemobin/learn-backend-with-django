# Generated by Django 4.0.6 on 2022-08-11 08:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('Icon_url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_category', to='products.productscategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('subtitle', models.CharField(max_length=512)),
                ('image1_url', models.URLField(blank=True, null=True)),
                ('image2_url', models.URLField(blank=True, null=True)),
                ('image3_url', models.URLField(blank=True, null=True)),
                ('image4_url', models.URLField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('SEK', 'Swedish Crown'), ('USD', 'American Dollar'), ('EUR', 'Euro'), ('GBP', 'Pound sterling'), ('JPY', 'Yen'), ('AUD', 'Australian Dollar')], default='USD', max_length=3)),
                ('variation_product_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.maker')),
            ],
        ),
    ]
