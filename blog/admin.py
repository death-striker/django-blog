from django.contrib import admin
from .models import RegisterUser, BlogPost
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model= RegisterUser
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('id',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'avatar')}),
    )


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__email')
    list_filter = ('created_at',)

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(RegisterUser, CustomUserAdmin)

