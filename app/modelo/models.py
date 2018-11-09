from django.db import models

# Create your models here.

class Estudiante(models.Model):
    listaGenero=(
        ('f', 'Femenino'),
        ('m', 'Masculino')
    )
    cedula=models.CharField(max_length=10, unique=True)
    numero=models.CharField(max_length=20)
    carrera=models.CharField(max_length=15)
    nombres=models.CharField(max_length=60)
    apellidos=models.CharField(max_length=60)
    edad=models.DateField(auto_now=False)
    genero=models.CharField(max_length=15, choices=listaGenero)
    estado=models.BooleanField(default=True)
