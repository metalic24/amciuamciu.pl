# Generated by Django 4.0 on 2022-01-04 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_img_path'),
        ('zamowienia', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('zakonczone', 'zakonczone'), ('dostarczne', 'dostarczane'), ('oplacone', 'oplacone'), ('przyjete', 'przyjete'), ('przygotowywane', 'przygotowywane')], default='przyjete', max_length=20),
        ),
    ]
