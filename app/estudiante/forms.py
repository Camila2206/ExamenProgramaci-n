from django import forms
from app.modelo.models import Estudiante

class FormularioEstudiante(forms.ModelForm):

    class Meta:
        model=Estudiante
        fields=["cedula", "numero", "carrera", "nombres", "apellidos" , "edad", "genero"]
