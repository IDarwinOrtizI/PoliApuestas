# Generated by Django 5.1.7 on 2025-03-28 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Partidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_apuesta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_apuesta', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('ganada', 'Ganada'), ('perdida', 'Perdida')], default='activa', max_length=20)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partidos.partido')),
            ],
        ),
    ]
