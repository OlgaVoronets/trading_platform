# Generated by Django 5.0.5 on 2024-05-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='products',
            field=models.ManyToManyField(to='retail.product', verbose_name='Продукты'),
        ),
    ]