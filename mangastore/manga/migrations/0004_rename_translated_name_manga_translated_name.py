# Generated by Django 4.1.4 on 2022-12-28 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0003_manga_translated_name_manga_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='Translated_name',
            new_name='translated_name',
        ),
    ]
