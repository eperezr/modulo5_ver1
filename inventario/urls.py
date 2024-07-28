from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categorias', views.CategoriasViewSet)


urlpatterns = [
    path('contact/<str:name>/',views.contact, name='contact'),
    path('categorias/', views.categorias, name='categorias'),
    path('tiendacbba/', views.productoFormView, name='tiendacbba'),
    path('tiendalp/', views.productoFormView, name='tiendalp'),
    path('tiendasc/', views.productoFormView, name='tiendasc'),
    path('', views.index),
    path('', include(router.urls))
]
