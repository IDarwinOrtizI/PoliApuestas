# rifas/urls.py
from django.urls import path
from .views import RifaListView, RifaCreateView, RifaUpdateView, RifaDeleteView

urlpatterns = [
    path('rifas/', RifaListView.as_view(), name='rifa_list'),
    path('rifas/create/', RifaCreateView.as_view(), name='rifa_create'),
    path('rifas/update/<int:pk>/', RifaUpdateView.as_view(), name='rifa_update'),
    path('rifas/delete/<int:pk>/', RifaDeleteView.as_view(), name='rifa_delete'),
]