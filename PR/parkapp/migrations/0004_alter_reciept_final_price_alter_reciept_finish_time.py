# Generated by Django 4.2.8 on 2023-12-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0003_alter_reciept_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciept',
            name='final_price',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='finish_time',
            field=models.DateTimeField(null=True),
        ),
    ]
