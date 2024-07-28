from django import forms
from .models import TiendaCbba


class ProductForm(forms.ModelForm):
    class Meta:
        model = TiendaCbba
        fields = '__all__'
