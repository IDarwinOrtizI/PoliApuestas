# partidos/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Partido
from Deportes.models import Campeonato

class PartidoListView(ListView):
    model = Partido
    template_name = 'partidos/partido_list.html'

class PartidoCreateView(CreateView):
    model = Partido
    fields = ['campeonato', 'fecha_partido', 'marcador', 'estado']
    template_name = 'partidos/partido_form.html'
    success_url = reverse_lazy('partido_list')

class PartidoUpdateView(UpdateView):
    model = Partido
    fields = ['campeonato', 'fecha_partido', 'marcador', 'estado']
    template_name = 'partidos/partido_form.html'
    success_url = reverse_lazy('partido_list')

class PartidoDeleteView(DeleteView):
    model = Partido
    template_name = 'partidos/partido_confirm_delete.html'
    success_url = reverse_lazy('partido_list')