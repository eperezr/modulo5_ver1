from django.core.exceptions import ValidationError

def validation_categoria(value):
    if value == "No permitido":
        raise ValidationError("No es una opcion permitida")
    
def validar_nombre(value):
    if value == "Comida":
        raise ValidationError('%(value)s no es un texto permitido', params={'value': value})
