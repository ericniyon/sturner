# Generated by Django 3.0.1 on 2020-01-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporttype',
            name='igihe_itangirwa',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Icyumweru'), (2, 'Ukwezi'), (3, 'Igihembwe'), (4, 'Amezi atandatu'), (5, 'Umwaka')]),
        ),
    ]