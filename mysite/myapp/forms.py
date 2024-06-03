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
        widgets = {
            "title": forms.TextInput(attrs={"class": "form__field"}),
            "description": forms.TextInput(attrs={"class": "form__field"}),
            "price": forms.NumberInput(attrs={"class": "form__field"}),
            "image": forms.FileInput(attrs={"class": "form__field"}),
            "cat": forms.Select(attrs={"class": "form__field"}),
            "slug": forms.TextInput(attrs={"class": "form__field"}),
        }
