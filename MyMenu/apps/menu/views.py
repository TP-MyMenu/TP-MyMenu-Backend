from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from MyMenu.apps.menu.models import Dish, DishCategory, Drink, DayDish
from MyMenu.apps.menu.serializers import DishSerializer, DishCategorySerializer, DrinkSerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, ]


class DishCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    permission_classes = [IsAuthenticated, ]


class DrinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAuthenticated, ]


class DayDishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DayDish.objects.all()
    serializer_class = DayDishSerializer
    permission_classes = [IsAuthenticated, ]
