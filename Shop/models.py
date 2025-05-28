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
    parents = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

class ParentCategory(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100, null=True, blank=True),
    )
    Category = models.ManyToManyField(Category, blank=True, related_name='parent_categories')
    
    class Meta:
        verbose_name = 'Əsas Kateqoriya'
        verbose_name_plural = 'Əsas Kateqoriyalar'

class Product(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        content = models.TextField()
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    categories = models.ManyToManyField(Category, blank=True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'
