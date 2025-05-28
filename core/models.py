from django.db import models
from parler.models  import TranslatableModel, TranslatedFields

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Setting(BaseModel):
    logo = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    address = models.TextField()
    language = models.CharField(max_length=10)
    language_flag = models.ImageField(upload_to='language_flags/')
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    pinterest = models.CharField(max_length=100)
    newsletter = models.CharField(max_length=100)
    newsletter_description = models.TextField()

    def __str__(self):
        return 'Ayarlar'
    
    def has_add_permission(self, request):
        if not request.user.is_staff:
            return False
        return False
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_staff:
            return False
        return False
    
    class Meta:
        verbose_name = 'Parametr'
        verbose_name_plural = 'Parametrlər'

    