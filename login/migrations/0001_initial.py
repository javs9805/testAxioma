# Generated by Django 4.2.5 on 2023-09-09 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombres', models.CharField(max_length=100, null=True)),
                ('apellidos', models.CharField(max_length=100, null=True)),
                ('numero_de_cuenta', models.CharField(max_length=20)),
                ('saldo_contable', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_disponible_cuenta_corriente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_disponible_linea_credito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_cargos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_abonos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
