# Generated by Django 4.2.6 on 2023-11-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='assest',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='com',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='lap',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='other',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='retcom',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='retlap',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='retother',
            field=models.IntegerField(null=True),
        ),
    ]
