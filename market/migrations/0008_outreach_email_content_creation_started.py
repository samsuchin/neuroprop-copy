# Generated by Django 4.2.6 on 2024-01-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_outreach_email_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreach',
            name='email_content_creation_started',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]