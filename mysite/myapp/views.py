from django.db.models.base import Model as Model
from .models import Product, Category
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .utils import DataMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import addProductForm
from django.urls import reverse_lazy


class TechHome(DataMixin, TemplateView):
    """Главная страница"""

    template_name = "myapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class TechCategory(DataMixin, ListView):
    """Просмотр категории"""

    template_name = "myapp/products.html"
    context_object_name = "items"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_queryset(self):
        if self.request.GET.get("search"):
            return get_list_or_404(
                Product,
                Q(title__icontains=self.request.GET.get("search"))
                | Q(description__icontains=self.request.GET.get("search")),
            )
        elif self.kwargs.get("category_slug") == "all":
            return Product.objects.all()
        else:
            return get_list_or_404(Product, cat__slug=self.kwargs.get("category_slug"))


class ShowProduct(DataMixin, DetailView):
    """Просмотр продукта"""

    model = Product
    template_name = "myapp/product_item.html"
    context_object_name = "item"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs.get(self.slug_url_kwarg))


class addProduct(CreateView):
    """Добавление продукта"""

    form_class = addProductForm
    template_name = "myapp/add_product.html"
    extra_context = {"categories": Category.objects.all()}


class UpdateProduct(UpdateView):
    """Редактирование продукта"""

    model = Product
    fields = ["title", "description", "price", "cat"]
    success_url = reverse_lazy("myapp:home")
    template_name = "myapp/add_product.html"
    extra_context = {"categories": Category.objects.all()}


class DeleteProduct(DeleteView):
    """Удаление продукта"""

    model = Product
    success_url = reverse_lazy("myapp:home")
