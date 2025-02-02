from rest_framework import serializers

from category_foods.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField()

    def get_foods(self, obj):
        published_foods = getattr(obj, 'published_food', [])
        return FoodSerializer(published_foods, many=True).data

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
