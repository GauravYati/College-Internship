# Generated by Django 4.1.7 on 2023-02-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
