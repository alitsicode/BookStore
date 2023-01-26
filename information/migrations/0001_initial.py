# Generated by Django 4.1.4 on 2022-12-17 19:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50, verbose_name='Shop_name')),
                ('description', models.TextField(verbose_name='description')),
                ('reward', models.TextField(blank=True, null=True, verbose_name='reward')),
                ('work_image', models.ImageField(upload_to='work_image', verbose_name='Images')),
                ('inventors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='inventors')),
            ],
            options={
                'verbose_name': 'About us',
            },
        ),
    ]