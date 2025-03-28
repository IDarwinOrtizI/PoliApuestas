# rifas/admin.py
from django.contrib import admin
from .models import Rifa, Boleteria

admin.site.register(Rifa)
admin.site.register(Boleteria)