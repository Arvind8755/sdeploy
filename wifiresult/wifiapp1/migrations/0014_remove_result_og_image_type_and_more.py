# Generated by Django 5.2.1 on 2025-06-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifiapp1', '0013_result_og_image_type_result_twitter_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='og_image_type',
        ),
        migrations.RemoveField(
            model_name='result',
            name='twitter_card',
        ),
        migrations.AddField(
            model_name='result',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
