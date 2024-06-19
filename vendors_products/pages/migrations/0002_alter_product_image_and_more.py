# Generated by Django 5.0.6 on 2024-06-18 12:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="pages/static"
                ),
                upload_to="product_images/",
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="companyBackgroundPicture",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="pages/static"
                ),
                upload_to="company_background_pics/",
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="companyDisplayPicture",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="pages/static"
                ),
                upload_to="company_display_pics/",
            ),
        ),
    ]
