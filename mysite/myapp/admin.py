from django.contrib import admin
from .models import Product, Category

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    list_filter = ("title",)
    search_fields = ("title", "price")
    ordering = ("title", "price")
