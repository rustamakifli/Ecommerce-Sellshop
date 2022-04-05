# Generated by Django 4.0.2 on 2022-04-05 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('parent_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mysweetchild', to='product.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
            ],
            options={
                'verbose_name': 'Product review',
                'verbose_name_plural': 'Product reviews',
            },
        ),
        migrations.CreateModel(
            name='PropertyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_property_name', to='product.category')),
            ],
            options={
                'verbose_name': 'Property name',
                'verbose_name_plural': 'Propert names',
            },
        ),
        migrations.CreateModel(
            name='PropertyValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_name_property_value', to='product.propertyname')),
            ],
            options={
                'verbose_name': 'Property values',
                'verbose_name_plural': 'Property values',
            },
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('is_main', models.BooleanField()),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_product_version', to='product.product')),
                ('publications', models.ManyToManyField(to='product.PropertyValues')),
            ],
            options={
                'verbose_name': 'Product version',
                'verbose_name_plural': 'Product versions',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/story_images/')),
                ('is_main', models.BooleanField()),
                ('product_version', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.productversion')),
            ],
            options={
                'verbose_name': 'Product images',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='product.product')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
    ]
