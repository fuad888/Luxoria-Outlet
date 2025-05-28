from django.db import models
from core.models import BaseModel
from parler.models  import TranslatableModel, TranslatedFields

class ContactPage(TranslatableModel, BaseModel):
    translations = TranslatedFields(
        contact_title = models.CharField(max_length=255,blank=True, null=True),
    )
    contact_banner = models.FileField(upload_to='contact_banner/', blank=True, null=True)

    # def __str__(self):
    #     return self.safe_translation_getter('contact_title')

    class Meta:
        verbose_name = 'Əlaqə Səhifəsi'
        verbose_name_plural = 'Əlaqə Səhifələri'

class Subscribe(BaseModel):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Abunə'
        verbose_name_plural = 'Abunələr'
    
class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField ()
    message = models.TextField()
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'