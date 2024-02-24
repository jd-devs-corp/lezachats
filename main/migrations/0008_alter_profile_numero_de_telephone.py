# Generated by Django 4.2.6 on 2023-10-29 21:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_profile_fb_url_profile_numero_de_telephone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='numero_de_telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='CM', unique=True),
        ),
    ]