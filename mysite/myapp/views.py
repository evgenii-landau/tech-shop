from .models import Product
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .utils import DataMixin
from django.db.models import Q


class TechHome(DataMixin, TemplateView):
    template_name = "myapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class TechCategory(DataMixin, ListView):
    template_name = "myapp/products.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_queryset(self):
        if self.request.GET.get("search"):
            return get_list_or_404(
                Product,
                Q(title__icontains=self.request.GET.get("search"))
                | 
                Q(description__icontains=self.request.GET.get("search")),
            )
        elif self.kwargs.get("category_slug") == "all":
            return Product.objects.all()
        else:
            return get_list_or_404(Product, cat__slug=self.kwargs.get("category_slug"))


class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = "myapp/product_item.html"
    context_object_name = "item"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs.get(self.slug_url_kwarg))
