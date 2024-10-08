# Generated by Django 5.1 on 2024-08-29 08:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("redbox_core", "0039_alter_file_original_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessageTokenUse",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "use_type",
                    models.CharField(
                        choices=[("input", "input"), ("output", "output")],
                        default="input",
                        help_text="input or output tokens",
                        max_length=10,
                    ),
                ),
                ("model_name", models.CharField(blank=True, max_length=50, null=True)),
                ("token_count", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "chat_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="redbox_core.chatmessage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
