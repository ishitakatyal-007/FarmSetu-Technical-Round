from turtle import update
from django.urls import path
from .views import update_stats

app_name = 'prev_year_highlights'

urlpatterns = [
    path('', update_stats, name='update_stats'),
]