from rest_framework import serializers

from MyMenu.apps.menu.models import Dish, DishCategory


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory,
        fields = '__all__'
