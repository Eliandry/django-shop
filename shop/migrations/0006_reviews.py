# Generated by Django 2.0 on 2020-06-30 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200630_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Reviews', verbose_name='Родитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]