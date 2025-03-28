# apuestas/urls.py
from django.urls import path
from .views import ApuestaListView, ApuestaCreateView, ApuestaUpdateView, ApuestaDeleteView

urlpatterns = [
    path('apuestas/', ApuestaListView.as_view(), name='apuesta_list'),
    path('apuestas/create/', ApuestaCreateView.as_view(), name='apuesta_create'),
    path('apuestas/update/<int:pk>/', ApuestaUpdateView.as_view(), name='apuesta_update'),
    path('apuestas/delete/<int:pk>/', ApuestaDeleteView.as_view(), name='apuesta_delete'),
]