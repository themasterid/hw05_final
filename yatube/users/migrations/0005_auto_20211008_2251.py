# Generated by Django 2.2.16 on 2021-10-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211008_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=600, verbose_name='Сообщение'),
        ),
    ]