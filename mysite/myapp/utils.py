from .models import Category


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context["categories"] = Category.objects.all()
        return context
