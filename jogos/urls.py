from django.urls import path

from . import views

app_name = 'jogos'
urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('<int:jogo_id>/comentario/', views.create_comentario, name='comentario'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create', views.CategoryCreateView.as_view(), name='create-category'),
]