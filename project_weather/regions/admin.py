from django.contrib import admin

# Register your models here.
from .models import RegionModel

class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name']

    def has_add_permission(request, obj=None):
        return False
            
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(RegionModel, RegionAdmin)
