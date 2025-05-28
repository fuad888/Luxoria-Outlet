from django.contrib import admin
from .models import  Category, Product, ParentCategory, shoppage
from parler.admin import TranslatableAdmin



@admin.register(shoppage)
class ShopPageAdmin(TranslatableAdmin):
    list_translations = ('shop_title',)
    list_display = ('shop_banner','created_at',)

class ParentCategoryAdmin(TranslatableAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
admin.site.register(ParentCategory, ParentCategoryAdmin)

class CategoryAdmin(TranslatableAdmin):

    list_display = ('name','slug', 'parents', 'created_at')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'stock', 'image', 'slug', 'created_at')
    list_filter = ('categories',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)