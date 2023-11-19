from django.db import models
from django.conf import settings


class Jogo(models.Model):
    name = models.CharField(max_length=255)
    dia_jogo = models.DateField()
    placar = models.CharField(max_length=20)
    escudo_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.dia_jogo})'


class Comentario(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'