# Generated by Django 5.1.6 on 2025-04-20 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
                ('category_gif', models.CharField(max_length=200)),
                ('category_description', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'dinner_platters',
            },
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'pasta',
            },
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
            options={
                'db_table': 'regular_pizza',
            },
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'salad',
            },
        ),
        migrations.CreateModel(
            name='SavedCarts',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cart', models.TextField()),
            ],
            options={
                'db_table': 'saved_carts',
            },
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_choice', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category_description', models.TextField()),
            ],
            options={
                'db_table': 'sicilian_pizza',
            },
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_filling', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'sub',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'topping',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('order', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('delivered', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_order',
            },
        ),
    ]
