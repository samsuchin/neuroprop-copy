# Generated by Django 4.2.6 on 2024-01-22 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0026_document_client_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='client_comments',
            new_name='client_question',
        ),
    ]