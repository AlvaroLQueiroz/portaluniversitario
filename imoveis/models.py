from django.db import models

SEXO = (
	('m','Masculino'),
	('f','Feminino'),
	('x','Misto'),
	)
TIPO = (
	('1','República'),
	('2','Pensionato/Casa de família'),
	('3','Kitnet/Flat'),
	('4','Apartamento ou casa para dividir'),
	('5','Imovél para locação do tipo casa'),
	('6','Imovél para locação do tipo apartamento'),

	)

class Imoveis(models.Model):
    user = models.ForeignKey(Question, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    sexo = models.CharField(max_length=2, choices=SEXO)
    tipo = models.CharField(max_length=3, choices=TIPO)
    endereco = models.CharField(max_length=200)
    valor = models.FloatField()
    contato = models.TextField()
    detalhes = models.TextField()
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    aprovado = models.BooleanField(default=False)