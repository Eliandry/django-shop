# Generated by Django 2.2.12 on 2020-05-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.CharField(default='', max_length=120),
        ),
    ]