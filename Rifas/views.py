# rifas/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rifa

class RifaListView(ListView):
    model = Rifa
    template_name = 'rifas/rifa_list.html'

class RifaCreateView(CreateView):
    model = Rifa
    fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'max_participantes', 'valor_boleteria', 'premio_principal']
    template_name = 'rifas/rifa_form.html'
    success_url = reverse_lazy('rifa_list')

class RifaUpdateView(UpdateView):
    model = Rifa
    fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'max_participantes', 'valor_boleteria', 'premio_principal']
    template_name = 'rifas/rifa_form.html'
    success_url = reverse_lazy('rifa_list')

class RifaDeleteView(DeleteView):
    model = Rifa
    template_name = 'rifas/rifa_confirm_delete.html'
    success_url = reverse_lazy('rifa_list')