# Generated by Django 5.0.7 on 2024-08-08 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
