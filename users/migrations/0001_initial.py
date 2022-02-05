# Generated by Django 4.0.1 on 2022-02-05 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyBrand',
            fields=[
                ('BrandID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('BrandName', models.CharField(max_length=100)),
                ('NoOfCars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuyCar',
            fields=[
                ('BCarID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('BCarImage', models.BinaryField()),
                ('BCarName', models.CharField(max_length=100)),
                ('BNumOfCars', models.IntegerField()),
                ('BBrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.buybrand')),
            ],
        ),
        migrations.CreateModel(
            name='RentCar',
            fields=[
                ('RCarID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('RCarName', models.CharField(max_length=100)),
                ('RImage', models.BinaryField()),
                ('RCarPrice', models.IntegerField()),
                ('RFuel', models.CharField(max_length=100)),
                ('RMileage', models.FloatField()),
                ('RSeatingCapacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuySpecs',
            fields=[
                ('CarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.buycar')),
                ('Image', models.BinaryField()),
                ('Price', models.FloatField()),
                ('Rating', models.IntegerField()),
                ('Mileage', models.FloatField()),
                ('CC', models.IntegerField()),
                ('SeatingCapacity', models.IntegerField()),
                ('Bootspace', models.IntegerField()),
                ('BodyType', models.CharField(max_length=100)),
                ('FuelType', models.CharField(max_length=100)),
                ('NoOfCylinders', models.IntegerField()),
                ('TransmissionType', models.CharField(max_length=100)),
                ('FuelCapacity', models.FloatField()),
                ('ServiceCost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SellCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SBrandName', models.CharField(max_length=100)),
                ('SCarName', models.CharField(max_length=100)),
                ('SCarPrice', models.IntegerField()),
                ('KmRun', models.IntegerField()),
                ('CarAge', models.IntegerField()),
                ('SFuel', models.CharField(max_length=100)),
                ('SMileage', models.FloatField()),
                ('SSeatingCapacity', models.IntegerField()),
                ('SCustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RentBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FromDate', models.DateField()),
                ('ToDate', models.DateField()),
                ('NoOfDays', models.IntegerField()),
                ('RentPerDay', models.IntegerField()),
                ('TotalRent', models.IntegerField()),
                ('RPhoneNum', models.BigIntegerField()),
                ('RAddress', models.TextField()),
                ('RCarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rentcar')),
                ('RCustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
