from django.urls import path, include
from . import views
from .views import TipoViewSet, ItemViewSet,NegocioListAndCreateView,NegocioRetrieveUpdateDeleteView,get_negocios_for_current_user
from rest_framework import routers



router =routers.DefaultRouter()
router.register('tipo-negocio',TipoViewSet)
# router.register('negocio',NegocioViewSet)
router.register('item',ItemViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/negocio/',NegocioListAndCreateView.as_view(),name='negocio'),
    path('api/negocio/<int:pk>/',NegocioRetrieveUpdateDeleteView.as_view(),name='negocioDetalles'),
    path('api/misnegocios/',views.get_negocios_for_current_user,name='misnegocios')
]