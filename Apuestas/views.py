# apuestas/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Apuesta

class ApuestaListView(ListView):
    model = Apuesta
    template_name = 'apuestas/apuesta_list.html'

class ApuestaCreateView(CreateView):
    model = Apuesta
    fields = ['partido', 'monto_apuesta']
    template_name = 'apuestas/apuesta_form.html'
    success_url = reverse_lazy('apuesta_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario autenticado
        return super().form_valid(form)

class ApuestaUpdateView(UpdateView):
    model = Apuesta
    fields = ['partido', 'monto_apuesta']
    template_name = 'apuestas/apuesta_form.html'
    success_url = reverse_lazy('apuesta_list')

class ApuestaDeleteView(DeleteView):
    model = Apuesta
    template_name = 'apuestas/apuesta_confirm_delete.html'
    success_url = reverse_lazy('apuesta_list')