# Generated by Django 4.2.6 on 2023-12-13 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prospect', '0006_prospect_amount'),
        ('tracker', '0011_remove_document_description_remove_document_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='prospect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_types', to='prospect.prospect'),
        ),
    ]
