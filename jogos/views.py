from django.http import HttpResponse
from .temp_data import jogos_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail(request, jogo_id):
    context = {'jogo': jogos_data[jogo_id - 1]}
    return render(request, 'jogos/detail.html', context)


def list(request):
    context = {"jogos_list": jogos_data}
    return render(request, 'jogos/index.html', context)


def create(request):
    if request.method == 'POST':
        jogos_data.append({
            'name': request.POST['name'],
            'dia_jogo': request.POST['dia_jogo'],
            'escudo_url': request.POST['escudo_url']
        })
        return HttpResponseRedirect(
            reverse('jogos:detail', args=(len(jogos_data), )))
    else:
        return render(request, 'jogos/create.html', {})