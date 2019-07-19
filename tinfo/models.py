from django.db import models

# Create your models here.

class Tripinfo(models.Model):
	name = models.CharField(max_length=200)
	data_de_partida = models.DateTimeField('data de partida')
	destino = models.CharField(max_length=200)
	data_de_chegada = models.DateTimeField('data de chegada')
	motorista = models.CharField(max_length=200)

	def __str__(self):
		return self.name + ' | ' + str(self.data_de_partida) + ' | ' + str(self.destino) + ' | ' + str(self.data_de_chegada) + ' | ' + str(self.motorista)
