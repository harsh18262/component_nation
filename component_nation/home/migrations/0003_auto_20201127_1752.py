# Generated by Django 3.1.2 on 2020-11-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_laptop_coding_30k_laptop_coding_40k_laptop_coding_50k_laptop_coding_base_laptop_gaming_30k_laptop_ga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop_coding_base',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='Laptop/Coding'),
        ),
        migrations.AlterField(
            model_name='laptop_gaming_base',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='Laptop/Gaming'),
        ),
    ]
