# Generated by Django 4.0.2 on 2022-03-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_delete_productpropertyvalues_brand_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_cat',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mysweetchild', to='product.category'),
        ),
    ]
