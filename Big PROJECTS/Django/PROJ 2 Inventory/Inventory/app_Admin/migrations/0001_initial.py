# Generated by Django 4.1.7 on 2023-03-31 06:29

import app_Admin.models
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app_Admin.models.NameField(max_length=50, unique=True)),
                ('category', models.TextField(choices=[('Consumable', 'Consumable'), ('Non-Consumable', 'Non-Consumable')], max_length=20)),
                ('item_img', models.ImageField(upload_to='images/')),
                ('item_qty', models.IntegerField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]