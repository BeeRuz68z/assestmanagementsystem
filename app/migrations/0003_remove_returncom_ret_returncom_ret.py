# Generated by Django 4.2.6 on 2023-11-01 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_returncom_ret_returncom_ret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returncom',
            name='ret',
        ),
        migrations.AddField(
            model_name='returncom',
            name='ret',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.com'),
            preserve_default=False,
        ),
    ]
