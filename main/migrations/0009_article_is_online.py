# Generated by Django 4.2.6 on 2023-10-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_profile_numero_de_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_online',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
