# Generated by Django 4.1.4 on 2023-01-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_bookmark_books_alter_bookmark_user_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, upload_to='category_cover', verbose_name='cover'),
        ),
    ]