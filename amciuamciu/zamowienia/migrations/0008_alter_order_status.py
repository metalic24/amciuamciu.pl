# Generated by Django 4.0 on 2022-01-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0007_order_rest_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('oplacone', 'oplacone'), ('zakonczone', 'zakonczone'), ('dostarczne', 'dostarczane'), ('przygotowywane', 'przygotowywane'), ('przyjete', 'przyjete')], default='przyjete', max_length=20),
        ),
    ]
