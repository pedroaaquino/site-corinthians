from django.urls import path

from . import views

urlpatterns = [
    path('historia/', views.historia, name='historia'),
    path('', views.home, name='home'),
]