# Generated by Django 4.0.1 on 2022-11-16 06:13

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userrent_urentperday_alter_userrent_utotalrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrent',
            name='UImage',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.filepath),
        ),
    ]