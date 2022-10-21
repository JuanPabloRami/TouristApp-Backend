from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission


class EsGrupoBase(BasePermission):
    nombre_grupo = ''


    def has_permission(self, request, view):
        print(view)
        return request.user.groups.filter(name=self.nombre_grupo).exists()


class EsGrupoEmprendedor(EsGrupoBase):
    nombre_grupo = 'Emprendedor'


class EsGrupoTurista(EsGrupoBase):
    message = 'No pertenece al grupo turistas'
    nombre_grupo = 'Turista'


class EsIpPermitida(BasePermission):
    message = 'Ip no permitida'
    ip_bloque = ['http://localhost:8000/api/negocio/','http://localhost:8000/api/negocio/','http://localhost:8000/api/negocio/','http://localhost:8000/api/item/']

    def has_permission(self, request, view):
        return request.META['REMOTE_ADDR'] not in self.ip_bloque