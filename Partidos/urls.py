# partidos/urls.py
from django.urls import path
from .views import PartidoListView, PartidoCreateView, PartidoUpdateView, PartidoDeleteView
from Deportes.models import Campeonato 
urlpatterns = [
    path('partidos/', PartidoListView.as_view(), name='partido_list'),
    path('partidos/create/', PartidoCreateView.as_view(), name='partido_create'),
    path('partidos/update/<int:pk>/', PartidoUpdateView.as_view(), name='partido_update'),
    path('partidos/delete/<int:pk>/', PartidoDeleteView.as_view(), name='partido_delete'),
]