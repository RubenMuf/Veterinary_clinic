# Generated by Django 4.2.7 on 2023-12-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_pet_medical_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinarian',
            name='slugVet',
            field=models.SlugField(max_length=20, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
