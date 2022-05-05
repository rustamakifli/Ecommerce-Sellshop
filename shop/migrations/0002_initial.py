# Generated by Django 4.0.2 on 2022-05-05 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='basket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_basket_items', to='shop.basket'),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='product_version',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_version_basket_items', to='product.productversion'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
