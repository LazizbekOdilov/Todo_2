# Generated by Django 4.2.7 on 2023-11-10 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0002_rename_batafsil_reja_t_datail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reja',
            name='egasi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
