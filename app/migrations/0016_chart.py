# Generated by Django 4.2.6 on 2023-11-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_assest_otls'),
    ]

    operations = [
        migrations.CreateModel(
            name='chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assest', models.IntegerField()),
                ('com', models.IntegerField()),
                ('retcom', models.IntegerField()),
                ('lap', models.IntegerField()),
                ('retlap', models.IntegerField()),
                ('other', models.IntegerField()),
                ('retother', models.IntegerField()),
            ],
        ),
    ]
