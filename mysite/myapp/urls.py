from django.urls import path
from myapp.views import TechHome, TechCategory, ShowProduct, addPage

app_name = "myapp"

urlpatterns = [
    path("", TechHome.as_view(), name="home"),
    path("search/", TechCategory.as_view(), name="search"),
    path("<slug:category_slug>/", TechCategory.as_view(), name="category"),
    path("product/add_product/", addPage, name="addPage"),
    path("product/<slug:product_slug>/", ShowProduct.as_view(), name="product"),
]
