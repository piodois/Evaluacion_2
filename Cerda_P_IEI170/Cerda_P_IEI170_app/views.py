from django.shortcuts import render, redirect
from .models import Reserva
from .forms import FormReserva

def index(request):
    return render(request, 'index.html')

def listarReservas(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReserva()

    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')

    data = {'form': form}
    return render(request, 'agregar_reserva.html', data)

def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('/reservas')

def modificarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = FormReserva(instance=reserva)

    if request.method == 'POST':
        form = FormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/reservas')

    data = {'form': form}
    return render(request, 'agregar_reserva.html', data)