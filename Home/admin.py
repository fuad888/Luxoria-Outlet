from django.contrib import admin
from .models import Homepage, Banner, Carusel
from parler.admin import TranslatableAdmin

@admin.register(Homepage)
class HomepageAdmin(TranslatableAdmin):
    list_display = ('title','created_at', 'updated_at')
    

@admin.register(Banner)
class BannerAdmin(TranslatableAdmin):
    list_display = ('title', 'updated_at', 'created_at')
# Register your models here.

@admin.register(Carusel)
class CaruselAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at', 'updated_at')
