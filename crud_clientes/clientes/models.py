from typing import Any
from django.db import models

# Create your models here.

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="lenguaje")

    def __str__(self):
        fila=self.nombre
        return fila

class SO(models.Model):
    nom_so = models.CharField(max_length=100, verbose_name="SO")

    def __str__(self):
        fila=self.nom_so
        return fila
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    ap = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    am = models.CharField(max_length=50, verbose_name="Apellido Materno")
    foto = models.ImageField(upload_to="imagenes/",verbose_name="Foto", null=True)
    lenguaje=models.ForeignKey(Lenguaje,verbose_name="Lenguaje", on_delete=models.CASCADE)
    so = models.ForeignKey(SO, verbose_name="So", on_delete=models.CASCADE)

    def __str__(self):
        fila= str (self.id)+ "-"+ "Nombre" + self.nombre 
        return fila
    
    def delete(self,usiing=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()





