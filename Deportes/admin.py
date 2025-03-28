# deportes/admin.py
from django.contrib import admin
from .models import Deporte, Campeonato

admin.site.register(Deporte)
admin.site.register(Campeonato)