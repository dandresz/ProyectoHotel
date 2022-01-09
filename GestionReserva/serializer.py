from django.db.models import fields
from rest_framework import serializers
from GestionReserva.models import DetallesdeReserva

class DetallesdeReservaSerializer(serializers.ModelSerializer):
    #atributos que contiene nuesto Model Detalles de la Reserva
    class Meta:
        model = DetallesdeReserva
        fields = ('id', 'nombre', 'diasestadia', 'numerohabitaciones', 'montopordia','montototal', 'metodopago', 'tipodereserva')

