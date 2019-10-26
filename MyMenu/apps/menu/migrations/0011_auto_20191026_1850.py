# Generated by Django 2.2.4 on 2019-10-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20191026_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='suitable_for_celiacs',
            field=models.BooleanField(default=False, verbose_name='suitable for celiacs'),
        ),
        migrations.AddField(
            model_name='dish',
            name='suitable_for_vegetarians',
            field=models.BooleanField(default=False, verbose_name='suitable for vegetarians'),
        ),
    ]
