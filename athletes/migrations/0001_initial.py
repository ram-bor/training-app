# Generated by Django 3.1 on 2021-04-27 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
                ('threshold_hr', models.IntegerField()),
                ('run_longest_distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_type', models.CharField(choices=[('R', 'Run'), ('S', 'Swim'), ('B', 'Bike')], default='R', max_length=32)),
                ('date', models.DateField()),
                ('planned_duration', models.TimeField(blank=True, null=True)),
                ('duration', models.TimeField()),
                ('hour_avg', models.TimeField()),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='athletes.athlete')),
            ],
        ),
    ]
