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


class Category(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100, null=True, blank=True),
    )
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

class Product(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        content = models.TextField()
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
