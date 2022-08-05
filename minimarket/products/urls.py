from django.urls import path

from . import views

urlpatterns = [
    path("products", views.ProductListView.as_view(), name="products"),
    path("categories", views.CategoryListView.as_view(), name="categories"),
]
