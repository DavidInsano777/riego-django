from django.db import models

# Create your models here.
class Lectura(models.Model):
    humedad = models.IntegerField()
    riego = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)  # se guarda la fecha y hora automática

    def __str__(self):
        return f"{self.fecha} - Humedad: {self.humedad} - Riego: {self.riego}"
