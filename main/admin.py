from django.contrib import admin
from main.models import Categories, Manufactures, Products

admin.site.register(Categories)
admin.site.register(Manufactures)
# admin.site.register(Products)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # Отображение полей в списке объектов модели
    list_display = ["name", "article", "price", "discount", "quantity", "category", "manufacture", "status",
                    "created", "update"]

    # Поля, доступные для редактирования прямо в списке объектов модели
    list_editable = ["price", "discount", "quantity", "category", "manufacture", "status"]

    # Поля, по которым можно осуществлять поиск
    search_fields = ["name", "description", "article"]

    # Поля, по которым можно фильтровать список объектов модели
    list_filter = ["category", "manufacture", "status"]

    # Порядок и группы отображения полей в форме редактирования/создания объекта
    fields = [
        "name",
        "meta_title",
        "meta_description",
        "meta_keywords",
        "description",
        "category",
        "manufacture",
        "url_slag",
        ("price", "discount"),
        "quantity",
        "status",
        "image",
        "sort_order",
        "created",
        "update"
    ]

    # Поля только для чтения
    readonly_fields = ["created", "update"]
