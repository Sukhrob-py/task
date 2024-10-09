from django.urls import path

from .views import (
    GetProductListApiView,
    VegetablesListApiView,
    NewProductsListApiView,
    SearchProductsApiView,
    ProductsListByCategoryApiView
)

urlpatterns = [
    path("get-all/", GetProductListApiView.as_view()),
    path("vegetables/", VegetablesListApiView.as_view()),
    path("new/", NewProductsListApiView.as_view()),
    path("search/", SearchProductsApiView.as_view()),
    path("filter-by-category/", ProductsListByCategoryApiView.as_view()),
]
