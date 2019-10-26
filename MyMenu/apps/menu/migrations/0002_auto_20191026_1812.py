# Generated by Django 2.2.4 on 2019-10-26 18:12

import MyMenu.apps.menu.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, storage=MyMenu.apps.menu.models.OverwriteStorage(), upload_to='dishes/categories', verbose_name='image')),
            ],
            options={
                'verbose_name': 'dish category',
                'verbose_name_plural': 'dish categories',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, storage=MyMenu.apps.menu.models.OverwriteStorage(), upload_to='drinks/', verbose_name='image')),
                ('price', models.FloatField(default=0, verbose_name='price')),
            ],
            options={
                'verbose_name': 'drink',
                'verbose_name_plural': 'drinks',
            },
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'dish', 'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=MyMenu.apps.menu.models.OverwriteStorage(), upload_to='dishes/', verbose_name='image'),
        ),
        migrations.CreateModel(
            name='DayDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_day_dish', models.BooleanField(default=False)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_dishes', to='menu.Drink', verbose_name='drink')),
                ('garnish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Dish', verbose_name='garnish')),
                ('main_dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_dishes', to='menu.Dish', verbose_name='main dish')),
            ],
            options={
                'verbose_name': 'day dish',
                'verbose_name_plural': 'day dishes',
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=1, on_delete='dish category', related_name='dishes', to='menu.DishCategory'),
            preserve_default=False,
        ),
    ]