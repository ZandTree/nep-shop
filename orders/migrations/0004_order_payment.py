# Generated by Django 2.0.1 on 2019-04-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190414_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]