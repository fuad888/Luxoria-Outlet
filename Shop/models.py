from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields
from core.models import BaseModel

class shoppage(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        shop_title=models.CharField(max_length=100, blank=True, null=True),
    )
    shop_banner = models.ImageField(upload_to='shop_banner/')

    class meta:
        verbose_name = 'Mağaza Səhifəsi'
        verbose_name_plural = 'Mağaza Səhifələri'

class Color(BaseModel, TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(max_length=50, null=True, blank=True)
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    color_class = models.CharField(max_length=100, null=True, blank=True, help_text="sidebar__item__color sidebar__item__color--'add color'")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.safe_translation_getter('name', any_language=True) or "—")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "—"

    class Meta:
        verbose_name = 'Rəng'
        verbose_name_plural = 'Rənglər'


class Category(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100, null=True, blank=True),
    )
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "—"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

class Size(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rəng'
        verbose_name_plural = 'Rənglər'

class Product(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        content = models.TextField(),
        shipping_info = models.TextField(blank=True, null=True),
        description = models.TextField(blank=True, null=True),
        info = models.TextField(blank=True, null=True),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.safe_translation_getter('name', any_language=True)}")

        super().save(*args, **kwargs)

