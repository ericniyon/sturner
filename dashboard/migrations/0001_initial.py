# Generated by Django 2.2.2 on 2019-12-14 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cell',
                'verbose_name_plural': 'Cells',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'KPI',
                'verbose_name_plural': 'KPIs',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_sectors', to='dashboard.District')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectors',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Cell')),
            ],
            options={
                'verbose_name': 'Village',
                'verbose_name_plural': 'Villages',
            },
        ),
        migrations.CreateModel(
            name='Umuryango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number_of_member', models.PositiveIntegerField()),
                ('icyiciro', models.PositiveIntegerField()),
                ('irangamuntu', models.BigIntegerField()),
                ('status', models.BinaryField(default=0)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Cell')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sector')),
                ('umudugudu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='village_cell', to='dashboard.Village')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sector'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieved', models.PositiveIntegerField()),
                ('pending', models.PositiveIntegerField()),
                ('ibisigaye', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('year', models.PositiveIntegerField(default=2019)),
                ('kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kpi_results', to='dashboard.KPI')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_results', to='dashboard.Sector')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
                'unique_together': {('kpi', 'year', 'sector')},
            },
        ),
    ]
