# Generated by Django 4.2.7 on 2023-12-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_alter_pet_options_alter_pet_age_alter_pet_breed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onwer',
            options={'ordering': ['id'], 'verbose_name': 'Хозяин', 'verbose_name_plural': 'Хозяева'},
        ),
        migrations.AlterField(
            model_name='onwer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='onwer',
            name='firstname',
            field=models.CharField(max_length=10, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='onwer',
            name='lastname',
            field=models.CharField(max_length=15, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='onwer',
            name='tel',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
        migrations.AddIndex(
            model_name='onwer',
            index=models.Index(fields=['id'], name='clinic_onwe_id_871f67_idx'),
        ),
    ]