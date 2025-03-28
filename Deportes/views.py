# deportes/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Deporte, Campeonato

class DeporteListView(ListView):
    model = Deporte
    template_name = 'deportes/deporte_list.html'

class DeporteCreateView(CreateView):
    model = Deporte
    fields = ['nombre']
    template_name = 'deportes/deporte_form.html'
    success_url = reverse_lazy('deporte_list')

class DeporteUpdateView(UpdateView):
    model = Deporte
    fields = ['nombre']
    template_name = 'deportes/deporte_form.html'
    success_url = reverse_lazy('deporte_list')

class DeporteDeleteView(DeleteView):
    model = Deporte
    template_name = 'deportes/deporte_confirm_delete.html'
    success_url = reverse_lazy('deporte_list')