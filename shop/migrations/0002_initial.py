# Generated by Django 4.0.2 on 2022-06-20 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='shop.basket'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='product_version',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='product.productversion'),
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to=settings.AUTH_USER_MODEL),
        ),
    ]
