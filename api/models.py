from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.FloatField(help_text="Ingrese el peso en kilogramos")
    estatura = models.FloatField(help_text="Ingrese la estatura en metros")

    def calcular_imc(self):
        imc = self.peso / (self.estatura * self.estatura)
        return imc

    def calcular_categoria_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"


class Cliente(models.Model):
    usuario = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
