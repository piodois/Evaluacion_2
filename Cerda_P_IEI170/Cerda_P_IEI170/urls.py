from django.contrib import admin
from django.urls import path
from Cerda_P_IEI170_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservas/', views.listarReservas),  # Cambio de 'proyectos/' a 'reservas/'
    path('agregar/', views.agregarReserva),  # Cambio de 'agregaProyecto' a 'agregarReserva'
    path('eliminar/<int:id>/', views.eliminarReserva),  # Cambio de 'eliminarProyecto' a 'eliminarReserva'
    path('actualiza/<int:id>/', views.modificarReserva),  # Cambio de 'modificaProyecto' a 'modificarReserva'
]