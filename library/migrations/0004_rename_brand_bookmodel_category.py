# Generated by Django 5.0 on 2023-12-28 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_bookmodel_brand_bookmodel_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='brand',
            new_name='category',
        ),
    ]
