from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=150)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=100, unique=True)
    campeonatos = models.ManyToManyField("Campeonato", through="Campeonato3")

    def __str__(self):
        return self.nombre


class Campeonato(models.Model):
    nombre = models.CharField(max_length=250)
    nombre_ausp = models.CharField(max_length=20)
    equipos = models.ManyToManyField(Equipo, through="Campeonato3")

    def __str__(self):
        return f"{self.nombre} - {self.nombre_ausp}"


class Jugador(models.Model):
    nombre = models.CharField(max_length=150)
    posicion = models.CharField(max_length=20)
    nro_camiseta = models.IntegerField()
    sueldo = models.FloatField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Campeonato3(models.Model):
    anio = models.IntegerField()
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Campeonato.nombre} - {self.Equipo.nombre}"
    
    
