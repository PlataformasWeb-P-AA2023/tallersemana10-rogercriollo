# Generated by Django 4.2.2 on 2023-06-18 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('nombre_ausp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Campeonato3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('Campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('siglas', models.CharField(max_length=10)),
                ('username_twitter', models.CharField(max_length=100, unique=True)),
                ('campeonatos', models.ManyToManyField(through='futbolec.Campeonato3', to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('posicion', models.CharField(max_length=20)),
                ('nro_camiseta', models.IntegerField()),
                ('sueldo', models.FloatField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.equipo')),
            ],
        ),
        migrations.AddField(
            model_name='campeonato3',
            name='Equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.equipo'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='equipos',
            field=models.ManyToManyField(through='futbolec.Campeonato3', to='futbolec.equipo'),
        ),
    ]
