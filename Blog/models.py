from django.db import models
from core.models import BaseModel 
from accounts.models import MyUser
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

class Blogpage(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
    )

    image=models.ImageField(upload_to='blog_page_images/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Bloq Səhifəsi'
        verbose_name_plural = 'Bloq Səhifələri'

class Blogs(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        content=RichTextField(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    BlogCategory = models.ManyToManyField('BlogCategory', related_name='blogs', blank=True)
    search_by = models.ManyToManyField('SearchByInline', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class meta:
        verbose_name = 'Bloq'
        verbose_name_plural = 'Bloqlar'

class BlogCategory(BaseModel,TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255,null=True, blank=True),
        
    )
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class meta:
        verbose_name = 'Bloq Kateqoriyası'
        verbose_name_plural = 'Bloq Kateqoriyaları'


class News(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        content=RichTextField(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Xəbər'
        verbose_name_plural = 'Xəbərlər'

class SearchByInline(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        search_term=models.CharField(max_length=255),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search_term
    
    class Meta:
        verbose_name = 'Axtarış Termini'
        verbose_name_plural = 'Axtarış Terminləri'

    
