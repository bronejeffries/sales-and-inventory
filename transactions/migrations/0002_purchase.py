# Generated by Django 4.1.2 on 2022-10-22 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vendor'),
        ('store', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0, verbose_name='Price per item(Ksh)')),
                ('total_value', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='accounts.vendor')),
            ],
            options={
                'ordering': ['order_date'],
            },
        ),
    ]
