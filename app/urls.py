from django.urls import path, include
from . import views
from .views import TipoViewSet, NegocioViewSet, ItemViewSet
from rest_framework import routers



router =routers.DefaultRouter()
router.register('tipo-negocio',TipoViewSet)
router.register('negocio',NegocioViewSet)
router.register('item',ItemViewSet)


urlpatterns = [
    path('api/',include(router.urls))
]