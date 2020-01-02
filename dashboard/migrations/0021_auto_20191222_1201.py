# Generated by Django 2.2.2 on 2019-12-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20191222_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umuryango',
            name='status',
        ),
        migrations.AddField(
            model_name='umuryango',
            name='achieved',
            field=models.PositiveIntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='umuryango',
            name='target',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
