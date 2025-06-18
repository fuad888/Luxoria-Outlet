from django.contrib import admin
from .models import  Category, Product, shoppage
from parler.admin import TranslatableAdmin



@admin.register(shoppage)
class ShopPageAdmin(TranslatableAdmin):
    list_translations = ('shop_title',)
    list_display = ('shop_banner','created_at',)

class CategoryAdmin(TranslatableAdmin):
    list_display = ('name','slug', 'created_at')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'stock', 'categories', 'created_at', 'image', 'image1', 'image2', 'image3', 'image4')
    search_fields = ('name',)
    list_filter = ('categories',)

admin.site.register(Product, ProductAdmin)