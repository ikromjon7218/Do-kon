# Generated by Django 4.1.5 on 2023-03-03 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('rasm', models.FileField(upload_to='bolimlar')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('narx', models.FloatField()),
                ('brend', models.CharField(max_length=50)),
                ('davlat', models.CharField(max_length=50)),
                ('kafolat', models.CharField(max_length=50)),
                ('min_miqdor', models.PositiveSmallIntegerField(default=1)),
                ('tasdiqlangan', models.BooleanField(default=True)),
                ('yetkazish', models.CharField(default='3-4 kun', max_length=20)),
                ('mavjud', models.BooleanField(default=True)),
                ('chegirma', models.PositiveSmallIntegerField(default=0)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='mahsulotlar')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
