# Generated by Django 4.1.5 on 2023-03-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_izoh_mahsulot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='izoh',
            name='sana',
            field=models.DateField(auto_now=True),
        ),
    ]
