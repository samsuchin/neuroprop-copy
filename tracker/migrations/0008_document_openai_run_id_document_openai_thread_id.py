# Generated by Django 4.2.6 on 2023-11-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_document_openai_assistant_id_document_openai_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='openai_run_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='openai_thread_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
