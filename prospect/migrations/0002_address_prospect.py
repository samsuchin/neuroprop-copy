# Generated by Django 4.2.6 on 2023-11-10 00:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('prospect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('state', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('in-progress', 'In Progress'), ('correcting', 'Correcting'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('purpose', models.CharField(choices=[('refinance', 'Refinance'), ('construction', 'Construction')], max_length=100)),
                ('property_type', models.CharField(choices=[('hotel', 'Hotel'), ('self-storage', 'Self Storage')])),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prospect.address')),
            ],
        ),
    ]