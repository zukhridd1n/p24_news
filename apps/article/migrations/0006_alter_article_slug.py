# Generated by Django 5.0.7 on 2024-08-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_remove_article_image_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, unique=True),
        ),
    ]
