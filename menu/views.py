from django.db.models import Prefetch
from django.shortcuts import render

from .models import About, Category, Dish, GalleryPhoto


# Create your views here.
def menu(request):
    categories = Category.objects.prefetch_related(
        Prefetch("dishes", queryset=Dish.objects.filter(visible=True))
    )
    photos = list(GalleryPhoto.objects.all())
    logo = next((photo for photo in photos if "logo" in photo.image.name.lower()), None)
    photos = [photo for photo in photos if photo is not logo]
    about = About.objects.first()
    return render(
        request,
        "menu/menu.html",
        {"categories": categories, "photos": photos, "logo": logo, "about": about},
    )
