from django.contrib import admin
from .models import  Category, Product, shoppage, Size,Color
from parler.admin import TranslatableAdmin



@admin.register(shoppage)
class ShopPageAdmin(TranslatableAdmin):
    list_translations = ('shop_title',)
    list_display = ('shop_banner','created_at',)

class CategoryAdmin(TranslatableAdmin):
    list_display = ('name','slug', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('slug',)
admin.site.register(Category, CategoryAdmin)

@admin.register(Color)
class ColorAdmin(TranslatableAdmin):
    list_display = ('name', 'color_class',)
    readonly_fields = ('slug',)

class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'stock', 'created_at',)
    search_fields = ('name','price',)
    list_filter = ('categories',)
    list_translations = ('name', 'content', 'shipping_info', 'description', 'info')
    readonly_fields = ('slug',)

admin.site.register(Product, ProductAdmin)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    readonly_fields = ('slug',)