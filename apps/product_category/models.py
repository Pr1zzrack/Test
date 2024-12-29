from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталог"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class FormFrame(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Форма Оправы"
        verbose_name_plural = "Формы Оправы"

    def __str__(self):
        return self.name


class Structure(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Конструкция"
        verbose_name_plural = "Конструкции"

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class Affiliation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Принадлежность"
        verbose_name_plural = "Принадлежности"

    def __str__(self):
        return self.name


class TempleLength(models.Model):
    length = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Длина Заушника"
        verbose_name_plural = "Длины Заушников"

    def __str__(self):
        return self.length


class FrameSize(models.Model):
    size = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Размер Рамки"
        verbose_name_plural = "Размеры Рамок"

    def __str__(self):
        return self.size


class SizeBridgeNose(models.Model):
    size = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Размер Переносицы"
        verbose_name_plural = "Размеры Переносиц"

    def __str__(self):
        return self.size


class Collection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "бренд"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    form_of_frame = models.ForeignKey(FormFrame, on_delete=models.SET_NULL, null=True)
    structure = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.SET_NULL, null=True)
    temple_length = models.ForeignKey(
        TempleLength, on_delete=models.SET_NULL, null=True
    )
    frame_size = models.ForeignKey(FrameSize, on_delete=models.SET_NULL, null=True)
    size_bridge_nose = models.ForeignKey(
        SizeBridgeNose, on_delete=models.SET_NULL, null=True
    )
    brand = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def clean(self):
        if self.stock < 0:
            raise ValidationError({"price": "Price cannot be less than 0"})
        if self.stock < 0:
            raise ValidationError({"stock": "Stock cannot be less than 0"})

    def save(self, *args, **kwargs):
        self.clean()
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class ConnectionFilters(models.Model):
    FILTER_CHOICES = [
        ("name", "Название"),
        ("description", "Описание"),
        ("price_min", "Цена от"),
        ("price_max", "Цена до"),
        ("category", "Категория"),
        ("stock", "Наличие на складе"),
        ("manufacturer", "Производитель"),
        ("form_of_frame", "Форма оправы"),
        ("structure", "Конструкция"),
        ("material", "Материал"),
        ("affiliation", "Принадлежность"),
        ("temple_length", "Длина заушника"),
        ("frame_size", "Размер рамки"),
        ("size_bridge_nose", "Размер переносицы"),
        ("brand", "Бренд"),
        ("created_at", "Дата создания"),
        ("updated_at", "Дата обновления"),
        ("slug", "Slug"),
    ]

    filter_value = models.CharField(max_length=50, choices=FILTER_CHOICES)
    active_status = models.CharField(
        max_length=10,
        choices=[
            ("on", "Включен"),
            ("off", "Отключен"),
        ],
        default="off",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_filter_value_display()} - {self.get_active_status_display()}"

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"
