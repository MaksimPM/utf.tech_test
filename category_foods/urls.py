from django.urls import path

from category_foods.apps import CategoryFoodsConfig
from category_foods.views import FoodListAPIView

app_name = CategoryFoodsConfig.name

urlpatterns = [
    path('foods/', FoodListAPIView.as_view(), name='foods-list'),
]
