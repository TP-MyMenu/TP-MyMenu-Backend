from rest_framework import serializers

from MyMenu.apps.menu.models import Dish, DishCategory, Drink, DayDish, Suggestion, PaymentMethod


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    category = DishCategorySerializer()

    class Meta:
        model = Dish
        fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class DayDishSerializer(serializers.ModelSerializer):
    main_dish = DishSerializer()
    garnish = DishSerializer()
    drink = DrinkSerializer()
    dessert = DrinkSerializer()

    class Meta:
        model = DayDish
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
