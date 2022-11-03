from django.contrib import admin
from .models import Negocio, Tipo_Negocio, Departamento, Ciudad , Item, Comentario
# Register your models here.

admin.site.register(Negocio)
admin.site.register(Tipo_Negocio)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Item)
admin.site.register(Comentario)

