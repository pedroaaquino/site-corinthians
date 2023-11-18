from django.urls import path

from . import views

app_name = 'jogos'
urlpatterns = [
    path('', views.list, name='index'),
    path('create/', views.create, name='create'),
    path('<int:jogo_id>/', views.detail, name='detail'),
]