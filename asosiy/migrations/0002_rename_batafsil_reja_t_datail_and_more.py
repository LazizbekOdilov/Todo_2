# Generated by Django 4.2.7 on 2023-11-10 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reja',
            old_name='batafsil',
            new_name='t_datail',
        ),
        migrations.RenameField(
            model_name='reja',
            old_name='boshlanmagan',
            new_name='t_name',
        ),
        migrations.RenameField(
            model_name='reja',
            old_name='m_text',
            new_name='t_status',
        ),
    ]