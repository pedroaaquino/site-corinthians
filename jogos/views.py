from django.http import HttpResponse
from .temp_data import jogos_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Jogo
from django.shortcuts import render, get_object_or_404
from .models import Jogo
from .forms import JogoForm
from django.views import generic


class DetailView(generic.DetailView):
    model = Jogo
    template_name = 'jogos/detail.html'


class ListView(generic.ListView):
    model = Jogo
    template_name = 'jogos/index.html'


class CreateView(generic.CreateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'jogos/create.html'
    success_url = '/jogos'
    

class UpdateView(generic.UpdateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'jogos/update.html'
    success_url = '/jogos'

class DeleteView(generic.DeleteView):
    model = Jogo
    template_name = 'jogos/delete.html'
    success_url = '/jogos'
