# Generated by Django 5.1 on 2024-08-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redbox_core', '0037_file_ingest_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='aisettings',
            name='max_document_tokens',
            field=models.PositiveIntegerField(blank=True, default=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='context_window_size',
            field=models.PositiveIntegerField(default=128000),
        ),
    ]
