# Generated by Django 4.0.2 on 2022-04-24 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
