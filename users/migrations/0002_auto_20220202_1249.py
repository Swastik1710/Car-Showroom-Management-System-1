# Generated by Django 3.2 on 2022-02-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buycar',
            name='BCarImage',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='buyspecs',
            name='Image',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='rentcar',
            name='RImage',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]