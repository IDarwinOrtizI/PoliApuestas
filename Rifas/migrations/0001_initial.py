# Generated by Django 5.1.7 on 2025-03-28 18:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('max_participantes', models.IntegerField()),
                ('valor_boleteria', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premio_principal', models.TextField()),
                ('premios_secundarios', models.TextField(blank=True)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('cerrada', 'Cerrada'), ('sorteada', 'Sorteada')], default='activa', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Boleteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_boleto', models.CharField(max_length=50, unique=True)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('ganadora', 'Ganadora'), ('no_ganadora', 'No Ganadora')], default='activa', max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rifas.rifa')),
            ],
        ),
    ]
