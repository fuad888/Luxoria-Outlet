from django.contrib import admin
from Contact.models import Subscribe, Contact , ContactPage
from parler.admin import TranslatableAdmin



@admin.register(ContactPage)
class ContactPageAdmin(TranslatableAdmin):
    list_translations = ['contact_title']

@admin.register(Subscribe)
class Subscribe(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['is_active']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']
    list_per_page = 10

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at', 'is_read']
    list_filter = ['is_read']
    ordering = ['-created_at']
    list_per_page = 10
