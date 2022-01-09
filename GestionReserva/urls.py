from django.urls import path
from GestionReserva.views import DetallesdeReservaList
from rest_framework.urlpatterns import format_suffix_patterns
from GestionReserva.models import DetallesdeReserva

#se ha construido un arreglo para ver el listado de las reservas-

urlpatterns = [
    path ('', DetallesdeReservaList.as_view(), name="detallesdeReserva"),
]
urlpatterns = format_suffix_patterns(urlpatterns)