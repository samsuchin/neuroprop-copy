# Generated by Django 4.2.6 on 2024-01-17 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_alter_document_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='openai_checked_time',
        ),
        migrations.RemoveField(
            model_name='document',
            name='openai_document_check_run_id',
        ),
        migrations.RemoveField(
            model_name='document',
            name='openai_document_check_thread_id',
        ),
    ]
