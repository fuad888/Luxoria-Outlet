# Generated by Django 5.2 on 2025-05-27 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactpage',
            options={'verbose_name': 'Əlaqə Səhifəsi', 'verbose_name_plural': 'Əlaqə Səhifələri'},
        ),
        migrations.AlterModelOptions(
            name='contactpagetranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Əlaqə Səhifəsi Translation'},
        ),
        migrations.AlterModelOptions(
            name='subscribe',
            options={'verbose_name': 'Abunə', 'verbose_name_plural': 'Abunələr'},
        ),
    ]
