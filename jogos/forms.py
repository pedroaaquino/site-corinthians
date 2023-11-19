from django.forms import ModelForm
from .models import Jogo, Comentario


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

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }