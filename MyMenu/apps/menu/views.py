from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from MyMenu.apps.menu.models import Dish, DishCategory, Drink, DayDish, Suggestion, PaymentMethod
from MyMenu.apps.menu.serializers import DishSerializer, DishCategorySerializer, DrinkSerializer, DayDishSerializer, \
    SuggestionSerializer, PaymentMethodSerializer


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


class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer
    permission_classes = [IsAuthenticated, ]


class PaymentMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated, ]
