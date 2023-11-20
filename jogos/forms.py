from django.forms import ModelForm
from .models import Jogo


class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = [
            'name',
            'dia_jogo',
            'placar',
            'escudo_url',
        ]
        labels = {
            'name': 'Jogo',
            'dia_jogo': 'Data',
            'placar': 'Placar',
            'escudo_url': 'URL do Escudo',
        }

