from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import UserRegisterApiView,UserLoginApiView

urlpatterns = [
    path("signup/", UserRegisterApiView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("login/", UserLoginApiView.as_view()),
]
