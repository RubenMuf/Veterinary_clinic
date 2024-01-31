# Generated by Django 4.2.7 on 2023-12-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_pet_image_veterinarian_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slugPet',
            field=models.SlugField(max_length=20, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
