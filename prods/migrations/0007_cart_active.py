# Generated by Django 2.0.1 on 2019-03-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prods', '0006_auto_20190225_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
