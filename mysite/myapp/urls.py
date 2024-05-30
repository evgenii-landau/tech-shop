from django.urls import path
from myapp.views import index, category , get_product

app_name = "myapp"

urlpatterns = [
	path("", index, name="home"),
    path("<slug:category_slug>/", category, name="category"),
    path("products/<slug:product_slug>/", get_product, name="product"),
]
