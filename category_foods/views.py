from django.db.models import Prefetch, Sum
from rest_framework import generics
from rest_framework.permissions import AllowAny

from category_foods.models import FoodCategory, Food
from category_foods.serializers import FoodListSerializer


class FoodListAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        return FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True).prefetch_related(
                Prefetch('additional', queryset=Food.objects.filter(is_publish=True))
            ), to_attr='published_food')
        )
