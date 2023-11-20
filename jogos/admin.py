from django.contrib import admin

from .models import Jogo, Comentario, Category

admin.site.register(Jogo)
admin.site.register(Comentario)
admin.site.register(Category)