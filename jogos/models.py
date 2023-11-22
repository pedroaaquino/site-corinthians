from django.db import models
from django.conf import settings
from django.utils import timezone


class Jogo(models.Model):
    name = models.CharField(max_length=255)
    dia_jogo = models.DateField()
    placar = models.CharField(max_length=20)
    escudo_url = models.URLField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} ({self.dia_jogo})'


class Comentario(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    jogos = models.ManyToManyField(Jogo)

    def __str__(self):
        return f'{self.name}'