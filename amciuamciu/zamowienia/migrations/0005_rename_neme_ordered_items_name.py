# Generated by Django 4.0 on 2021-12-21 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordered_items',
            old_name='neme',
            new_name='name',
        ),
    ]
