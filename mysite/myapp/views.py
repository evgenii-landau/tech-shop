from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404, get_list_or_404


def index(requset):
    cat = Category.objects.all()
    context = {"categories": cat}
    return render(requset, "myapp/index.html", context=context)


def category(requset, category_slug):
    if category_slug == "all":
        items = Product.objects.all()
    else:
        items = get_list_or_404(Product, cat__slug=category_slug)

    cat = Category.objects.all()
    context = {"categories": cat, "items": items}
    return render(requset, "myapp/products.html", context=context)


def get_product(request, product_slug):
    item = get_object_or_404(Product, slug=product_slug)
    cat = Category.objects.all()
    context = {"categories": cat, "item": item}
    return render(request, "myapp/product_item.html", context=context)
