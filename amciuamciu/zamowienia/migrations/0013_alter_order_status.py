# Generated by Django 4.0 on 2022-01-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0012_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('dostarczne', 'dostarczane'), ('oplacone', 'oplacone'), ('przyjete', 'przyjete'), ('zakonczone', 'zakonczone'), ('przygotowywane', 'przygotowywane')], default='przyjete', max_length=20),
        ),
    ]
