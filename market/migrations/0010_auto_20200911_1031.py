# Generated by Django 3.1.1 on 2020-09-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20200911_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='direction',
            field=models.CharField(choices=[('Recieving', 'Recieving Bee Bonds'), ('Spending', 'Spending Bee Bonds')], default='Spending Bee Bonds', max_length=25),
        ),
    ]
