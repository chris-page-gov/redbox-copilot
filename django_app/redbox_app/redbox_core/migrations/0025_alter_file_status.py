# Generated by Django 5.0.7 on 2024-07-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("redbox_core", "0024_user_ai_experience_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="status",
            field=models.CharField(
                choices=[
                    ("uploaded", "Uploaded"),
                    ("parsing", "Parsing"),
                    ("chunking", "Chunking"),
                    ("embedding", "Embedding"),
                    ("indexing", "Indexing"),
                    ("complete", "Complete"),
                    ("unknown", "Unknown"),
                    ("deleted", "Deleted"),
                    ("errored", "Errored"),
                    ("processing", "Processing"),
                ]
            ),
        ),
    ]
