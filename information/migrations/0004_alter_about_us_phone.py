# Generated by Django 4.1.4 on 2023-01-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_about_us_instagram_about_us_linkdin_about_us_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='phone',
            field=models.CharField(default='9015738669', max_length=10, verbose_name='Phone number'),
        ),
    ]
