from . import views
from django.urls import path,include
from .views import ViewUsersView,ComentarioViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers
router =routers.DefaultRouter()
router.register('usersList',ViewUsersView)
router.register('comentario',ComentarioViewSet)


urlpatterns = [
    path('viewsets/',include(router.urls)),
    path("signup/",views.signUpView.as_view(),name="signup"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("jwt/create/",TokenObtainPairView.as_view(),name="jwt_create"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("jwt/verify/",TokenVerifyView.as_view(),name="token_verify"),
    path("request-password-reset/",views.RequestResetPwEmailView.as_view(),name="request-password-reset"),
    path("password-reset/<uidb64>/<token>/",views.PasswordTokenCheckView.as_view(),name="password-reset-confirm")
    
]

