from django.contrib import admin
from .models import Blogs, BlogCategory, News, SearchByInline, Blogpage
from parler.admin import TranslatableAdmin

@admin.register(Blogpage)
class BlogPageAdmin(TranslatableAdmin):
    list_translations = ('title',)
    list_display = ('image',)

    
@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('blogs')

@admin.register(Blogs)
class BlogAdmin(TranslatableAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('BlogCategory',)
    search_fields = ('title', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'user', 'BlogCategory', 'search_by','is_active','slug') 
        }),
    )

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'user', 'created_at')


@admin.register(SearchByInline)
class SearchByInline(TranslatableAdmin):
    list_display = ('search_term',)
    search_fields = ('search_term',)
