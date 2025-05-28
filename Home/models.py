from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from core.models import BaseModel


class Homepage(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        hero_title = models.CharField(max_length=100),
        hero_subtitle = models.CharField(max_length=100),
        hero_description = models.TextField()

    )
    hero_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ana Səhifə'
        verbose_name_plural = 'Ana Səhifələr'
    
class Banner(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
    )
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Bannerlər'
