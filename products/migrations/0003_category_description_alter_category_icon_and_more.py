# Generated by Django 5.2.1 on 2025-05-13 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_category_product_featured_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="icon",
            field=models.CharField(
                blank=True,
                help_text="Icon class name (ex: fas fa-tools)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="products.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="featured",
            field=models.BooleanField(
                default=False, help_text="Afficher ce produit en page d'accueil"
            ),
        ),
    ]
