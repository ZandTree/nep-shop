# Generated by Django 2.0.1 on 2019-04-14 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190406_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='order_unid',
        ),
    ]
