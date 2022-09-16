from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', UserListView.as_view(), name = 'listar_persona'),
    path('api/crear/', UserCreateView.as_view(), name = 'crear_persona'),
    path('api/actualiza/<int:pk>/', UserDetailView.as_view(), name = 'actualiza_persona'),
    path('api/borrar/<int:pk>/', UserDeleteView.as_view(), name = 'borrar_persona'),
]