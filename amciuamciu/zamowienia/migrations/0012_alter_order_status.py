# Generated by Django 4.0 on 2022-01-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('przygotowywane', 'przygotowywane'), ('przyjete', 'przyjete'), ('dostarczne', 'dostarczane'), ('zakonczone', 'zakonczone'), ('oplacone', 'oplacone')], default='przyjete', max_length=20),
        ),
    ]