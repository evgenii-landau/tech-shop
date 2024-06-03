from django.urls import path
from myapp.views import (
    TechHome,
    TechCategory,
    ShowProduct,
    addProduct,
    UpdateProduct,
    DeleteProduct,
)

app_name = "myapp"

urlpatterns = [
    path("", TechHome.as_view(), name="home"),
    path("search/", TechCategory.as_view(), name="search"),
    path("<slug:category_slug>/", TechCategory.as_view(), name="category"),
    path("product/add_product/", addProduct.as_view(), name="addPage"),
    path("product/<slug:product_slug>/", ShowProduct.as_view(), name="product"),
    path("product/<slug:slug>/update/", UpdateProduct.as_view(), name="updatePage"),
    path("product/<slug:slug>/delete/", DeleteProduct.as_view(), name="deletePage"),
]
