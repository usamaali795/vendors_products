# Generated by Django 5.0.1 on 2024-06-17 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("companyName", models.CharField(max_length=255)),
                ("established", models.DateField()),
                ("employeesCount", models.IntegerField()),
                ("internalProfessionalService", models.BooleanField()),
                ("lastDemo", models.DateField()),
                ("lastReview", models.DateField()),
                (
                    "companyDisplayPicture",
                    models.ImageField(upload_to="company_display_pics/"),
                ),
                (
                    "companyBackgroundPicture",
                    models.ImageField(upload_to="company_background_pics/"),
                ),
                ("company_url", models.URLField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("productName", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="product_images/")),
                ("business_area", models.CharField(max_length=255)),
                ("modules", models.CharField(max_length=255)),
                ("financialServicesClientTypes", models.CharField(max_length=255)),
                ("cloud", models.BooleanField()),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="pages.vendor",
                    ),
                ),
            ],
        ),
    ]
