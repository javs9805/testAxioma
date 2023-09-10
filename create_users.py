import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bancaweb.settings')
django.setup()

from django.contrib.auth.models import User
from login.models import Usuario


def crear_usuarios():
    superusuarios = User.objects.filter(is_superuser=True)
    if not superusuarios.exists():
        # Crea un superusuario
        superusuario = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        print('Superusuario creado:', superusuario)
        print('Clave superusuario: admin')
        # Crea un usuario de prueba
        usuario_prueba = User.objects.create_user(
            username=str(input("Ingrese su nombre: ")),
            email=str(input("Ingrese su correo: ")),
            password=str(input("Ingrese su contraseña: "))
        )
        rut = random.randint(100000, 999999)
        usuario = Usuario.objects.create(
            user=usuario_prueba,  
            rut=rut,
            nombres='Nombre',
            apellidos='Apellido',
            numero_de_cuenta='4411312',
            saldo_contable=1000.0,
            saldo_disponible_cuenta_corriente=800.0,
            saldo_disponible_linea_credito=200.0,
            total_cargos=500.0,
            total_abonos=700.0,
            intentos=0,
            estado='Activo'
        )
        print('Usuario de prueba creado, el rut es:', rut)
    else:
        print("No puede ejecutar esta funcion 2 veces")
if __name__ == '__main__':
    crear_usuarios()