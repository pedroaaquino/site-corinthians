from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'staticpages/home.html', context)


def historia(request):
    context = {}
    return render(request, 'staticpages/historia.html', context)