from django.urls import path
from myapp.views import index, products, get_product

app_name = "myapp"

urlpatterns = [
    path("", index),
    path("products/", products, name="products"),
    path("products/<slug:product_slug>", get_product, name="product"),
]
