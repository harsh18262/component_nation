# Generated by Django 3.1.3 on 2021-01-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
