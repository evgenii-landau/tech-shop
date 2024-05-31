from django.urls import path
from myapp.views import TechHome, TechCategory, ShowProduct

app_name = "myapp"

urlpatterns = [
    path("", TechHome.as_view(), name="home"),
    path("search/", TechCategory.as_view(), name="search"),
    path("<slug:category_slug>/", TechCategory.as_view(), name="category"),
    path("product/<slug:product_slug>/", ShowProduct.as_view(), name="product"),
]
