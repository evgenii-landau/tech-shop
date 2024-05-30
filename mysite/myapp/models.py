from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликованно")
    image = models.ImageField(
        upload_to="images/", blank=True, verbose_name="Изображение"
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        blank=True,
        unique=True,
        verbose_name="URL",
    )
    cat = models.ForeignKey(
        to="Category", on_delete=models.PROTECT, null=True, verbose_name="Категория"
    )

    def get_absolute_url(self):
        return reverse("myapp:product", kwargs={"product_slug": self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
