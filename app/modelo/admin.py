from django.contrib import admin

# Register your models here.
from .models import Estudiante

class AdminEstudiante(admin.ModelAdmin):

    list_display=["cedula", "numero", "carrera", "nombres", "apellidos", "edad" , "genero"]
    list_editable=["nombres", "genero"]
    search_fields=["cedula"]
    class Meta:
        model=Estudiante
admin.site.register(Estudiante, AdminEstudiante)
