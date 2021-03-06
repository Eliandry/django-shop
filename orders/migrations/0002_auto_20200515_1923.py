# Generated by Django 2.2.12 on 2020-05-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
