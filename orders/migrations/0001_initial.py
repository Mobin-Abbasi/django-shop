# Generated by Django 5.0.2 on 2024-02-25 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_product_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('address', models.CharField(max_length=250, verbose_name='ادرس')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('province', models.CharField(max_length=50, verbose_name='محل سکونت')),
                ('city', models.CharField(max_length=50, verbose_name='شهر')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False, verbose_name='وضعیت پرداخت')),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='orders_orde_created_743fca_idx')],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('weight', models.PositiveIntegerField(default=0, verbose_name='وزن')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
        ),
    ]
