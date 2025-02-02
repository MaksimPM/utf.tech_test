from django.contrib import admin

from category_foods.models import Food, FoodCategory

admin.site.register(Food)
admin.site.register(FoodCategory)
