from rest_framework import serializers

from MyMenu.apps.menu.models import Dish, DishCategory, Drink, DayDish, Suggestion


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory,
        fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class DayDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayDish
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'
