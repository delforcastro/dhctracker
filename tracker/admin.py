from django.contrib import admin

# Register your models here.

from .models import Cliente, Tarea

admin.site.register(Cliente)
admin.site.register(Tarea)
