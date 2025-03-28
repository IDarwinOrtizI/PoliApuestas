# cuentas/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser

class UserListView(ListView):
    model = CustomUser
    template_name = 'cuentas/user_list.html'

class UserCreateView(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'rol', 'estado']
    template_name = 'cuentas/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'rol', 'estado']
    template_name = 'cuentas/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'cuentas/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')