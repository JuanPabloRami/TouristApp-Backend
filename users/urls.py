from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path("signup/",views.signUpView.as_view(),name="signup"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("jwt/create/",TokenObtainPairView.as_view(),name="jwt_create"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("jwt/verify/",TokenVerifyView.as_view(),name="token_verify"),
    path("request-password-reset/",views.RequestResetPwEmailView.as_view(),name="request-password-reset"),
    path("password-reset/<uidb64>/<token>/",views.PasswordTokenCheckView.as_view(),name="password-reset-confirm")
]

