# Generated by Django 4.0 on 2022-01-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0013_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('zakonczone', 'zakonczone'), ('dostarczne', 'dostarczane'), ('przyjete', 'przyjete'), ('oplacone', 'oplacone'), ('przygotowywane', 'przygotowywane')], default='przyjete', max_length=20),
        ),
    ]
