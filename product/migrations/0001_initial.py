# Generated by Django 4.0.2 on 2022-05-22 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbsrtactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('title_en', models.CharField(db_index=True, max_length=50, null=True)),
                ('title_az', models.CharField(db_index=True, max_length=50, null=True)),
                ('parent_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category')),
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
            name='PropertyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_names', to='product.category')),
            ],
            options={
                'verbose_name': 'Property name',
                'verbose_name_plural': 'Property names',
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_values', to='product.propertyname')),
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
                ('title', models.CharField(db_index=True, max_length=50)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('is_main', models.BooleanField()),
                ('product', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_versions', to='product.product')),
                ('property', models.ManyToManyField(blank=True, to='product.PropertyValue')),
            ],
            options={
                'verbose_name': 'Product version',
                'verbose_name_plural': 'Product versions',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('is_main', models.BooleanField(default=False, verbose_name='Main picture')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('product_version', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.productversion')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='product.product')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('absrtactmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.absrtactmodel')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
                ('product_version', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.productversion')),
            ],
            options={
                'verbose_name': 'Product review',
                'verbose_name_plural': 'Product reviews',
            },
            bases=('product.absrtactmodel',),
        ),
    ]
