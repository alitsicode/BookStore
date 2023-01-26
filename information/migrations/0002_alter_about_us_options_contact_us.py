# Generated by Django 4.1.4 on 2022-12-18 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name': 'About u'},
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='your text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
