from django.contrib import admin
from core.models import Setting

@admin.register(Setting)
class Setting(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('logo', 'title', 'email', 'phone', 'address','postal_code', 'language','language_flag')
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'instagram', 'twitter', 'pinterest')
        }),
        ('Newsletter', {
            'fields': ('newsletter', 'newsletter_description')
        }),

    )