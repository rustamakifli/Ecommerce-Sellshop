# Generated by Django 4.0.2 on 2022-04-07 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('basket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basketid', to='shop.basket')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='BasketItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=6, max_digits=12)),
                ('count', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('basket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_basket_items', to='shop.basket')),
                ('product_version', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_version_basket_items', to='product.productversion')),
            ],
            options={
                'verbose_name': 'Basket item',
                'verbose_name_plural': 'Basket items',
            },
        ),
    ]
