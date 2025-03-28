# deportes/urls.py
from django.urls import path
from .views import DeporteListView, DeporteCreateView, DeporteUpdateView, DeporteDeleteView

urlpatterns = [
    path('deportes/', DeporteListView.as_view(), name='deporte_list'),
    path('deportes/create/', DeporteCreateView.as_view(), name='deporte_create'),
    path('deportes/update/<int:pk>/', DeporteUpdateView.as_view(), name='deporte_update'),
    path('deportes/delete/<int:pk>/', DeporteDeleteView.as_view(), name='deporte_delete'),
]