from django import forms
from reserva.models import Reserva
from datetime import date


class ReservaForm(forms.ModelForm):

    def clean_date(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para data do passado')
        return data

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes'
        ]