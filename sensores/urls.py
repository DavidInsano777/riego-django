from django.urls import path
from .views import lectura_api
from .views import recibir_lectura

urlpatterns = [
    path('lectura/', lectura_api),
    path('api/lectura/', recibir_lectura, name='recibir_lectura'),
]
