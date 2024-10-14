# Generated by Django 5.1.1 on 2024-10-11 09:21

import django.core.validators
from django.db import migrations, models


def back_populate_ai_settings(apps, schema_editor):
    AISettings = apps.get_model("redbox_core", "AISettings")
    for ai_settings in AISettings.objects.all():
        ai_settings.self_route_enabled = False
        ai_settings.recursion_limit = 50
        ai_settings.match_name_boost = 2.0
        ai_settings.match_description_boost = 0.5
        ai_settings.match_keywords_boost = 0.5
        ai_settings.save()



class Migration(migrations.Migration):

    dependencies = [
        ('redbox_core', '0049_user_accessibility_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aisettings',
            name='match_description_boost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.5, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='aisettings',
            name='match_keywords_boost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.5, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='aisettings',
            name='match_name_boost',
            field=models.DecimalField(blank=True, decimal_places=2, default=2.0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='aisettings',
            name='recursion_limit',
            field=models.PositiveIntegerField(blank=True, default=50, null=True),
        ),
        migrations.AddField(
            model_name='aisettings',
            name='self_route_enabled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='knn_boost',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='match_boost',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='rag_gauss_scale_decay',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='rag_gauss_scale_max',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='rag_gauss_scale_min',
            field=models.DecimalField(decimal_places=2, default=1.1, max_digits=5, validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='similarity_threshold',
            field=models.DecimalField(decimal_places=2, default=0.7, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.RunPython(back_populate_ai_settings, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='aisettings',
            name='match_description_boost',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='match_keywords_boost',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='match_name_boost',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='recursion_limit',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='aisettings',
            name='self_route_enabled',
            field=models.BooleanField(default=False),
        ),

    ]