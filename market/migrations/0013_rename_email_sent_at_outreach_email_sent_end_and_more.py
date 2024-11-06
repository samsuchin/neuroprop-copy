# Generated by Django 4.2.6 on 2024-02-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_outreach_email_sent_at_outreach_email_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outreach',
            old_name='email_sent_at',
            new_name='email_sent_end',
        ),
        migrations.AddField(
            model_name='outreach',
            name='email_sent_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]