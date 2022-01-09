from django.db import models

# Create your models here.
TIPO_RESERVA=(
    ('pendiente','Pendiente'),
    ('pagado','Pagado'),
    ('eliminado','Eliminado')
)

TIPO_PAGO=(
    ('tarjeta','Tarjeta'),
    ('efectivo','Efectivo')
)



class DetallesdeReserva(models.Model):
    
    nombre=models.CharField(max_length=30, verbose_name="Nombre Cliente")
    diasestadia=models.IntegerField(verbose_name="Dias de estadia")
    numerohabitaciones=models.IntegerField(verbose_name="Numero de habitacion")
    montopordia=models.IntegerField(verbose_name="Precio por dia")
    montototal= models.IntegerField(verbose_name="Precio total")
    metodopago=models.CharField(max_length=20, choices= TIPO_PAGO, verbose_name="Tipo de Pago")
    tipodereserva=models.CharField(max_length=20, choices= TIPO_RESERVA,verbose_name="Reserva")

    def __str__(self):
        return self.nombre
    
    def montototal(self):
        return self.diasestadia * self.montopordia
