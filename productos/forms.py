from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'cantidad', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el nombre'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe la descripción del producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

        labels = {
            'nombre': 'nombre',
            'descripcion': 'descripcion',
            'precio' : 'precio',
            'categoria' : 'categoria',
            'cantidad' : 'cantidad',
            'imagen' : '',
        }
