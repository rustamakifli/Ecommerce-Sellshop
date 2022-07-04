# Generated by Django 4.0.2 on 2022-07-03 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=250)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.SlugField(editable=False, max_length=70)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Blog brand',
                'verbose_name_plural': 'Blog brands',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('blog', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blog')),
                ('parent_comment', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='blog.blogcomment')),
            ],
            options={
                'verbose_name': 'Blog comment',
                'verbose_name_plural': 'Blog comments',
            },
        ),
    ]
