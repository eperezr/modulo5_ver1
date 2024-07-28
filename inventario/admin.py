from django.contrib import admin
from .models import Categoria, TiendaCbba, TiendaLP, TiendaSC, Aduna

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible',)
    list_filter = ('disponible', 'categoria',)
    search_fields = ('nombre',)
    ordering = ('precio',)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(TiendaCbba, ProductAdmin)
admin.site.register(TiendaLP, ProductAdmin)
admin.site.register(TiendaSC, ProductAdmin)
admin.site.register(Aduna, ProductAdmin)