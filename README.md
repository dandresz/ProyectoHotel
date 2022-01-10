# ProyectoHotel

Crear entorno virtual:
C:\Users\..\Documents\>python -m venv entorpython -m venv entorno
Activando el entorno virtual, ubicandose en la carpeta donde ha creado el entorno
C:\Users\..\Documents\..>entorno\Scripts\activate
(entorno) C:\Users\..\Documents\..>
INSTALANDO LOS PAQUETES QUE UTILIZAREMOS:
(entorno) C:\Users\..\Documents\..>pip install Django==2.2.2
(entorno) C:\Users\..\Documents\..>pip install djangorestframework
(entorno) C:\Users\..\Documents\..>pip install markdown       # Markdown support for the browsable API.
(entorno) C:\Users\..\Documents\..>pip install django-filter  # Filtering support
 (entorno) C:\Users\..\Documents\..>pip install psycopg2
(entorno) C:\Users\..\Documents\..>cd ProyectoDjango

(entorno) C:\Users\..\Documents\..\ProyectoDjango>django-admin startproject Hotel

(entorno) C:\Users\..\Documents\..\ProyectoDjango>cd Hotel

(entorno) PS C:\Users\..\Documents\..\ProyectoDjango\Hotel> python manage.py migrate

(entorno) PS C:\Users\..\Documents\..\ProyectoDjango\Hotel> python manage.py startapp GestionReserva

PARA CUANDO SE CREA MODELS NUEVOS O ACTUALIZADOS
(entorno) PS C:\Users\..\Documents\..\ProyectoDjango\Hotel> python manage.py makemigrations

PARA QUE LOS MODELOS VAYAN A LA BD
(entorno) PS C:\Users\..\Documents\..\ProyectoDjango\Hotel> python manage.py sqlmigrate GestionReserva 0001

PARA QUE LAS TABLAS VAYAN A LA BD
(entorno) PS C:\Users\..\Documents\..\ProyectoDjango\Hotel> python manage.py migrate

django admin
usuario: daniel
pass:  daniel123

PARA ACCEDER:
http://127.0.0.1:8000/detallesdeReserva/


Endpoints propuestos para listar y registrar las reservas: GET , POST
Los serializer son clases que nos permiten transformar nuestros datos que obtener de Model y lo transforma en un formato JSON

GET para listar los datos de la reserva. Podremos visualizar los datos:
los detalles del cuarto reservado e identificacion del cliente:
nombre del cliente, dias de estadia, tipo de reserva(pagado,eliminado y pendiente)
Detalles de la facturacion:
Monto por dia, nombre del cliente, monto pagado(monto total), metodo de pago(Tarjeta o efectivo).

POST para registrar una reserva
