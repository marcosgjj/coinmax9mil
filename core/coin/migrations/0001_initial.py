# Generated by Django 4.1 on 2022-08-15 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
                ('dateCoin', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
