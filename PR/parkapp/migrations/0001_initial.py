# Generated by Django 4.2.5 on 2023-12-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
    ]