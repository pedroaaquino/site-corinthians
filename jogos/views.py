from django.http import HttpResponse
from .temp_data import jogos_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Jogo
from django.shortcuts import render, get_object_or_404
from .models import Jogo, Comentario
from .forms import JogoForm, ComentarioForm
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

def create_comentario(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_author = form.cleaned_data['author']
            comentario_text = form.cleaned_data['text']
            comentario = Comentario(author=comentario_author,
                            text=comentario_text,
                            jogo=jogo)
            comentario.save()
            return HttpResponseRedirect(
                reverse('jogos:detail', args=(jogo_id, )))
    else:
        form = ComentarioForm()
    context = {'form': form, 'jogo': jogo}
    return render(request, 'jogos/comentario.html', context)