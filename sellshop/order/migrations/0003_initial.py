# Generated by Django 4.0.2 on 2022-07-12 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='wishlistofUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='order.country'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='order.basket'),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='basketitems', to='order.basket'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='productVersion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Product_Cart', to='product.productversion', verbose_name='Product Version'),
        ),
        migrations.AddField(
            model_name='basket',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
