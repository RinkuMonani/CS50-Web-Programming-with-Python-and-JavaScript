# Generated by Django 2.0.3 on 2018-11-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_pizza_typeofpizza'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='description',
            field=models.CharField(default='', max_length=128),
        ),
    ]
