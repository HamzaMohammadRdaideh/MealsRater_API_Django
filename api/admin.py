from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Meal, Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','meal','user','stars']
    list_filter = ['meal','user']

class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    search_fields = ['title','description']
    list_filter = ['title','description']

# Register your models here.
admin.site.register(Rating, RatingAdmin)
admin.site.register(Meal, MealAdmin)
