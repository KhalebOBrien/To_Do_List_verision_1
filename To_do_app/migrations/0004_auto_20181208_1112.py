# Generated by Django 2.1.4 on 2018-12-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_app', '0003_auto_20181208_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='activity',
            field=models.CharField(blank='True', max_length=200),
        ),
    ]
