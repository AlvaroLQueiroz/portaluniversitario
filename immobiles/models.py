from django.db import models
from django.contrib.auth.models import User

GENDERS = (
    ('m','Masculino'),
    ('f','Feminino'),
    ('x','Misto'),
    )
KINDS = (
    ('1','República'),
    ('2','Pensionato/Casa de família'),
    ('3','Kitnet/Flat'),
    ('4','Apartamento ou casa para dividir'),
    ('5','Imovél para locação do tipo casa'),
    ('6','Imovél para locação do tipo apartamento'),

    )

class Immobile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    title = models.CharField(max_length=200, verbose_name='Título')
    gender = models.CharField(max_length=2, choices=GENDERS, verbose_name='Sexo')
    kind = models.CharField(max_length=3, choices=KINDS, verbose_name='Tipo de imóvel')
    address = models.CharField(max_length=200, verbose_name='Endereço')
    value = models.FloatField(verbose_name='Valor')
    contact = models.TextField(verbose_name='Contato')
    details = models.TextField(verbose_name='Detalhes')
    latitude = models.CharField(max_length=200, verbose_name='')
    longitude = models.CharField(max_length=200, verbose_name='')
    approved = models.BooleanField(default=False, verbose_name='Aprovado')
