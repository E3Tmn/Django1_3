# Generated by Django 4.2.9 on 2025-03-01 00:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]
