from django.contrib import admin

# Register your models here.
from .models import YearlyStatisticsModel

class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['year', 'region', 'category', 'highlight_stats']
    list_filter = ['region', 'category']

    def has_add_permission(request, obj=None):
        return False
            
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(YearlyStatisticsModel, StatisticsAdmin)