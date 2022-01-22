from django.contrib import admin

# Register your models here.
from .models import CriterionModel

admin.site.site_header = 'UK Meteorology'
admin.site.site_title = ''
admin.site.index_title = ''

class CriterionAdmin(admin.ModelAdmin):
    list_display = ['criterion_name']

    def has_add_permission(request, obj=None):
        return False
            
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CriterionModel, CriterionAdmin)
