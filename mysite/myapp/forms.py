from django import forms
from .models import Category, Product


class addProductForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Категория",
        empty_label="Категория не выбрана",
    )

    class Meta:
        model = Product
        fields = ["title", "description", "price", "image", "cat", "slug"]
