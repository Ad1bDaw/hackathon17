# Generated by Django 2.0.1 on 2018-01-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_auto_20180104_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
