from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from GestionReserva.models import DetallesdeReserva
from GestionReserva.serializer import DetallesdeReservaSerializer

#Listar(get) y registrar(post) las reservas y ver el monto total , asi como tambien los demas datos
#many=True para el listado de todos los objetos
class DetallesdeReservaList(APIView):

    def get(self, request, format=None):
        detallesdeReserva = DetallesdeReserva.objects.all()
        serializer = DetallesdeReservaSerializer(detallesdeReserva, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = DetallesdeReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
