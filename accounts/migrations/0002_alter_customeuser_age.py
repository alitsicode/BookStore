# Generated by Django 4.1.4 on 2022-12-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
