# Generated by Django 4.2.6 on 2023-11-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_document_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]