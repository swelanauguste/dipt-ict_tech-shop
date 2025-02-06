from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListview.as_view(), name="product-list"),
    path("detail/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product-delete"),
]
