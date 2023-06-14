from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    opcoes = [
        ('professor1', 'Sandro'),
        ('professor2', 'Nilton'),
        ('professor3', 'Orlando')
    ]
    professor = models.CharField(max_length=100, choices=opcoes)
