# Generated by Django 4.1.4 on 2023-02-06 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='firstname')),
                ('last_name', models.CharField(max_length=50, verbose_name='lastname')),
                ('address', models.CharField(max_length=400, verbose_name='address')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone')),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal_code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
