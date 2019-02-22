from django import forms
from . import models
 

class NuevaNoti(forms.ModelForm):
    class Meta:
        model = models.NuevaNot
        fields = ['titulo','fecha','descripcion','link','imagen']

class LogU(forms.ModelForm):
    class Meta:
        model = models.UserLog
        fields = ['nombre','clave']