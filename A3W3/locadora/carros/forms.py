from django import forms
from .models import Carro, Reserva

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'preco_diaria']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['carro', 'usuario', 'data_reserva', 'data_devolucao']
