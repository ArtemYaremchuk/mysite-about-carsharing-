# Generated by Django 3.0.2 on 2020-05-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentalCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_start', models.CharField(max_length=50, verbose_name='Дата начала аренды')),
                ('data_end', models.CharField(max_length=50, verbose_name='Дата окончания аренды')),
                ('name', models.CharField(max_length=50, verbose_name='Имя заказчика')),
                ('number', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('message', models.CharField(max_length=300, verbose_name='Сообщение')),
                ('rental', models.BooleanField(default=False, verbose_name='Аренда с залогом')),
                ('rental_without', models.BooleanField(default=False, verbose_name='Аренда без залога')),
                ('wheels_glass_insurance', models.BooleanField(default=False, verbose_name='Страховка колес и стекла')),
                ('rental_navigator', models.BooleanField(default=False, verbose_name='Аренда навигатора')),
                ('child_seat_rental', models.BooleanField(default=False, verbose_name='Аренда детского кресла')),
                ('Unlimited_mileage', models.BooleanField(default=False, verbose_name='Неограниченый пробег')),
            ],
            options={
                'verbose_name': 'Аренда',
                'verbose_name_plural': 'Аренда заказы',
            },
        ),
    ]
