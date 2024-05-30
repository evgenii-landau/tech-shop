from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404


nav_data = [
    {"name": "Все продукты", "url": "products/"},
    {"name": "Телефоны", "url": "phone/"},
    {"name": "Планшеты", "url": "tablet/"},
    {"name": "Ноутбуки", "url": "laptop/"},
    {"name": "Часы", "url": "watch/"},
    {"name": "Наушники", "url": "headphones/"},
    {"name": "Телевизоры", "url": "tv/"},
]


def index(requset):
    context = {"nav_data": nav_data}
    return render(requset, "myapp/index.html", context=context)


def products(requset):
    items = Product.objects.all()
    context = {"nav_data": nav_data, "title": "HomePage", "items": items}
    return render(requset, "myapp/products.html", context=context)


def get_product(request, product_slug):
    item = get_object_or_404(Product, slug=product_slug)
    context = {"nav_data": nav_data, "item": item}
    return render(request, "myapp/product_item.html", context=context)
