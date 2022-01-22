from email.headerregistry import Group
from django.contrib import admin

from django.contrib.auth.models import User, Group
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
from .models import CategoryModel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

    def has_add_permission(request, obj=None):
        return False
            
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CategoryModel, CategoryAdmin)