# Generated by Django 4.1.4 on 2023-01-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_category_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ip_address')),
            ],
        ),
    ]
