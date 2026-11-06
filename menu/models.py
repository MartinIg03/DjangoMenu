from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField("name (English)", max_length=100, blank=True)
    note = models.CharField(max_length=100, blank=True)
    note_en = models.CharField("note (English)", max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="dishes"
    )
    name = models.CharField(max_length=100)
    name_en = models.CharField("name (English)", max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    description_en = models.CharField(
        "description (English)", max_length=300, blank=True
    )
    price = models.FloatField()
    photo = models.ImageField(upload_to="dishes/", blank=True)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class GalleryPhoto(models.Model):
    image = models.ImageField(
        upload_to="gallery/", width_field="width", height_field="height"
    )
    width = models.PositiveIntegerField(null=True, editable=False)
    height = models.PositiveIntegerField(null=True, editable=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    @property
    def shape(self):
        if not self.width or not self.height:
            return "square"
        ratio = self.width / self.height
        if ratio > 1.25:
            return "wide"
        if ratio < 0.8:
            return "tall"
        return "square"


class About(models.Model):
    title = models.CharField(max_length=100, default="За Нас")
    title_en = models.CharField(
        "title (English)", max_length=100, default="About Us", blank=True
    )
    text = models.TextField(blank=True)
    text_en = models.TextField("text (English)", blank=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title
