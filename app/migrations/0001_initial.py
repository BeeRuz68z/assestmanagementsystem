# Generated by Django 4.2.6 on 2023-11-01 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empls', models.CharField(max_length=50)),
                ('systy', models.CharField(max_length=50)),
                ('otls', models.CharField(max_length=50)),
                ('gdt', models.DateField()),
                ('rdt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Com',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comname', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('hdd', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('cpnm', models.CharField(max_length=50)),
                ('cpsn', models.CharField(max_length=50)),
                ('monname', models.CharField(max_length=50)),
                ('mnsn', models.CharField(max_length=50)),
                ('prcl', models.CharField(max_length=50)),
                ('grcname', models.CharField(max_length=50)),
                ('gcs', models.CharField(max_length=50)),
                ('kyname', models.CharField(max_length=50)),
                ('msname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=50)),
                ('empemail', models.CharField(max_length=50)),
                ('empdob', models.DateField()),
                ('empmbno', models.IntegerField()),
                ('empage', models.IntegerField()),
                ('empid', models.CharField(max_length=50)),
                ('emppos', models.CharField(max_length=50)),
                ('empjndt', models.DateField()),
                ('empexp', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lapname', models.CharField(max_length=50)),
                ('los', models.CharField(max_length=50)),
                ('lhdd', models.CharField(max_length=50)),
                ('lram', models.CharField(max_length=50)),
                ('lcm', models.CharField(max_length=50)),
                ('lsn', models.CharField(max_length=50)),
                ('prcl', models.CharField(max_length=50)),
                ('grcname', models.CharField(max_length=50)),
                ('gcs', models.CharField(max_length=50)),
                ('canv', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Otheracc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyboard', models.CharField(max_length=50)),
                ('mouse', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobno', models.IntegerField()),
                ('postion', models.CharField(max_length=50)),
                ('staffid', models.CharField(max_length=50)),
                ('pasw', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Returncom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ret', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.com')),
            ],
        ),
    ]