from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'address', 'phone', 'created_at']
    search_fields = ['username', 'email', 'address', 'phone', 'created_at']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('address', 'phone', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(MyUser, MyUserAdmin)