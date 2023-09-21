from django.contrib import admin


# Register your models here.
from .models import Cliente, Atendente, Departamento, Situacao
admin.site.register(Cliente)
admin.site.register(Atendente)
admin.site.register(Departamento)
admin.site.register(Situacao)
