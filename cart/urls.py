from django.urls import path

from .views import (
    AddToCartApiView,
    GetUserCartApiView,
    ClearCartApiView,
    DeleteProductCartApiView,
)

urlpatterns = [
    path("add/", AddToCartApiView.as_view()),
    path("get/", GetUserCartApiView.as_view()),
    path("clear/", ClearCartApiView.as_view()),
    path("delete/", DeleteProductCartApiView.as_view()),
]
