from django.contrib import admin

from .models import About, Category, Dish, GalleryPhoto


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "name_en", "note", "note_en", "order")
    list_editable = ("note", "order")


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "name_en",
        "category",
        "formatted_price",
        "visible",
        "order",
    )
    list_editable = ("order", "visible")
    list_filter = ("category",)
    search_fields = ("name",)

    @admin.display(description="Price", ordering="price")
    def formatted_price(self, obj):
        return f"{obj.price:.2f} €"


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("image", "order")
    list_editable = ("order",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()
