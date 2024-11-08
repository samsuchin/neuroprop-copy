# Generated by Django 4.2.6 on 2024-02-20 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0018_note_is_smart_alter_note_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LenderSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField(default=dict)),
                ('status', models.CharField(choices=[('unprocessed', 'Unprocessed'), ('matched', 'Matched'), ('unmatched', 'Unmatched'), ('not_relevant', 'Not Relevant')], default='unprocessed', max_length=100)),
                ('lender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='syncs', to='market.lender')),
                ('note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='syncs', to='market.note')),
            ],
        ),
    ]
