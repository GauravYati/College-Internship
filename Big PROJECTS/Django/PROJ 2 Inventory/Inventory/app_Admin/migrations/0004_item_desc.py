# Generated by Django 4.1.7 on 2023-04-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Admin', '0003_item_category_main_remove_item_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(default=' ', max_length=200),
        ),
    ]
