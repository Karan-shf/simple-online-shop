# Generated by Django 5.0.3 on 2024-03-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_product_image_url_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]