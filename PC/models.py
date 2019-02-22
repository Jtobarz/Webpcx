from django.db import models
# Create your models here.

class NuevaNot(models.Model):
    titulo = models.CharField(max_length=500)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to=(''))

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.titulo,self.fecha,self.descripcion,self.link,self.imagen)


class UserLog(models.Model):
    nombre = models.CharField(max_length=50)
    clave = models.CharField(max_length=12)

    def __str__(self):
        return "{0} {1}".format(self.nombre,self.clave)