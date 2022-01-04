# Generated by Django 4.0 on 2022-01-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0005_rename_neme_ordered_items_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('dostarczne', 'dostarczane'), ('przyjete', 'przyjete'), ('oplacone', 'oplacone'), ('zakonczone', 'zakonczone'), ('przygotowywane', 'przygotowywane')], default='przyjete', max_length=20),
        ),
    ]
