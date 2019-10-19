from rest_framework import serializers

from MyMenu.apps.menu.models import Dish
from MyMenu.apps.menu.models import Drink

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
