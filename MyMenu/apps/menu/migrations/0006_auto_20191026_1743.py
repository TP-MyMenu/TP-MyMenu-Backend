# Generated by Django 2.2.4 on 2019-10-26 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20191026_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daydish',
            name='garnish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Dish', verbose_name='garnish'),
        ),
    ]