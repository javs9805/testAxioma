from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100, null=True)
    apellidos = models.CharField(max_length=100, null=True)
    numero_de_cuenta = models.CharField(max_length=20)
    saldo_contable = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_disponible_cuenta_corriente = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_disponible_linea_credito = models.DecimalField(max_digits=10, decimal_places=2)
    total_cargos = models.DecimalField(max_digits=10, decimal_places=2)
    total_abonos = models.DecimalField(max_digits=10, decimal_places=2)
    intentos = models.IntegerField(default=0)
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    # Agrega otros campos de perfil según tus necesidades

    def __str__(self):
        return self.user.username

