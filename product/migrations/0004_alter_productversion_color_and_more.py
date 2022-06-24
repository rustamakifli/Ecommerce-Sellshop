# Generated by Django 4.0.2 on 2022-06-24 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productversion_color_alter_productversion_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='color',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='same_color_product_versions', to='product.color'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_versions', to='product.product'),
        ),
    ]
