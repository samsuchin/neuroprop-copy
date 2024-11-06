# Generated by Django 4.1 on 2022-10-03 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_accountlink_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountlink',
            name='linked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accountlink',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]