from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404


nav_data = [
    {"name": "Store", "url": "products/"},
    {"name": "Mac", "url": "mac/"},
    {"name": "iPad", "url": "ipad/"},
    {"name": "iPhone", "url": "iphone/"},
    {"name": "Watch", "url": "watch/"},
    {"name": "Vision", "url": "vision/"},
    {"name": "AirPods", "url": "airpods/"},
    {"name": "Tv & Home", "url": "tv_home/"},
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
