# Generated by Django 4.2.6 on 2023-11-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
