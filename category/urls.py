from django.urls import path

from .views import GetCategoryListApiView, GetDiscountCategoryListApiView

urlpatterns = [
    path("get/", GetCategoryListApiView.as_view()),
    path("get/discount/", GetDiscountCategoryListApiView.as_view()),
]
