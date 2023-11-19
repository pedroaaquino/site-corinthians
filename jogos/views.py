from django.http import HttpResponse
from .temp_data import jogos_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Jogo
from django.shortcuts import render, get_object_or_404

def detail(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    context = {'jogo': jogo}
    return render(request, 'jogos/detail.html', context)


def list(request):
    jogo_list = Jogo.objects.all()
    context = {"jogo_list": jogo_list}
    return render(request, 'jogos/index.html', context)


def create(request):
    if request.method == 'POST':
        jogo_name = request.POST['name']
        jogo_dia_jogo = request.POST['dia_jogo']
        jogo_escudo_url = request.POST['escudo_url']
        jogo_placar = request.POST['placar']
        jogo = Jogo(name=jogo_name,
                      dia_jogo=jogo_dia_jogo,
                      escudo_url=jogo_escudo_url,
                      placar=jogo_placar)
        jogo.save()
        return HttpResponseRedirect(
            reverse('jogos:detail', args=(jogo.id, )))
    else:
        return render(request, 'jogos/create.html', {})
    
def update(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)

    if request.method == "POST":
        jogo.name = request.POST['name']
        jogo.dia_jogo = request.POST['dia_jogo']
        jogo_escudo_url = request.POST['escudo_url']
        jogo_placar = request.POST['placar']
        
        jogo.save()
        return HttpResponseRedirect(
            reverse('jogos:detail', args=(jogo.id, )))

    context = {'jogo': jogo}
    return render(request, 'jogos/update.html', context)

def delete(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)

    if request.method == "POST":
        jogo.delete()
        return HttpResponseRedirect(reverse('jogos:index'))

    context = {'jogo': jogo}
    return render(request, 'jogos/delete.html', context)