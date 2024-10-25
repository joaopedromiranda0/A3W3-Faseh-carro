from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  
from .models import Carro, Reserva
from .forms import CarroForm, ReservaForm

def listar_carros(request):
    query = request.GET.get('q')
    if query:
        carros = Carro.objects.filter(Q(marca__icontains=query) | Q(modelo__icontains=query))
    else:
        carros = Carro.objects.all()
    return render(request, 'carros/lista_carros.html', {'carros': carros})

def criar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm()
    return render(request, 'carros/form_carro.html', {'form': form})

def editar_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carros/form_carro.html', {'form': form})

def deletar_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        carro.delete()
        return redirect('listar_carros')
    return render(request, 'carros/deletar_carro.html', {'carro': carro})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'carros/lista_reservas.html', {'reservas': reservas})

def criar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'carros/form_reserva.html', {'form': form})
