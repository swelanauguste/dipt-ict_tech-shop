from carts.forms import CartAddProductForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .models import Product


class ProductListview(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CartAddProductForm
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product-list")
