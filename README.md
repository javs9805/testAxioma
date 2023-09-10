# Test Tecnico Axioma
Desarrollo en django en el cual se puede iniciar sesion de acuerdo a un rut y contraseña de usuario. 
![This is an alt text.](/static/images/picture1.png "This is a sample image.")

En caso de fallar 3 veces el inicio de sesión la cuenta del usuario se inactiva.
![This is an alt text.](/static/images/picture3.png "This is a sample image.")

Solamente el admin, por medio de djangoAdmin y accediendo al modelo Usuarios, puede volver a activar la cuenta de un usuario que se encuentra inactiva
![This is an alt text.](/static/images/picture4.png "This is a sample image.")

En caso de iniciar sesion correctamente, se muestra un dashboard indicando los datos de la cuenta y un botón para poder cerrar sesión
![This is an alt text.](/static/images/picture2.png "This is a sample image.")



## Herramientas

* Python 3.11.5
* Django 4.2.5

## Comandos para la ejecución
1. Primeramente debemos clonar el repositorio a nuestra computadora con el siguiente comando
```
git clone https://github.com/javs9805/testAxioma.git
```

2. Crear un entorno virtual:
```
python -m venv venv
```
Esto creará un entorno virtual llamado "venv" en la carpeta de su proyecto.

3. Activar el entorno virtual:

En Windows:
```
venv\Scripts\activate
```

En macOS/Linux:
```
source venv/bin/activate
```

4. Instalar las dependencias del proyecto:

```
pip install -r requirements.txt
```
Esto instalará todas las bibliotecas y paquetes necesarios para su proyecto.


5. Aplicar las migraciones de la base de datos:

```
python manage.py makemigrations
python manage.py migrate
```
Esto configurará la base de datos según las definiciones de su proyecto.

6. Ejecutar el servidor de desarrollo de Django:

```
python manage.py runserver
```

Ahora, el proyecto debería estar en funcionamiento y accesible en http://localhost:8000/ en su navegador web.

7. Crear usuarios de prueba:

Cree el superusuario y un usuario de prueba ejecutando el siguiente comando y siguiendo las instrucciones que indica el script:

```
python create_users.py
```
