# Generated by Django 2.2.4 on 2019-10-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20191026_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='client name')),
                ('suggestion', models.CharField(max_length=300, verbose_name='suggestion')),
            ],
        ),
    ]
