from django.http import HttpResponse
from .temp_data import jogos_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Jogo
from django.shortcuts import render, get_object_or_404
from .models import Jogo
from .forms import JogoForm

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
        form = JogoForm()
    context = {'form': form}
    return render(request, 'jogos/create.html', context)
    
def update(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)

    if request.method == "POST":
        form = JogoForm(request.POST)
        if form.is_valid():
            jogo.name = form.cleaned_data['name']
            jogo.dia_jogo = form.cleaned_data['dia_jogo']
            jogo.placar = form.cleaned_data['placar']
            jogo.escudo_url = form.cleaned_data['escudo_url']
            jogo.save()
            return HttpResponseRedirect(
                reverse('jogos:detail', args=(jogo.id, )))
    else:
        form = JogoForm(
            initial={
                'name': jogo.name,
                'dia_jogo': jogo.dia_jogo,
                'placar': jogo.placar,
                'escudo_url': jogo.escudo_url
            })

    context = {'jogo': jogo, 'form': form}
    return render(request, 'jogos/update.html', context)

def delete(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)

    if request.method == "POST":
        jogo.delete()
        return HttpResponseRedirect(reverse('jogos:index'))

    context = {'jogo': jogo}
    return render(request, 'jogos/delete.html', context)