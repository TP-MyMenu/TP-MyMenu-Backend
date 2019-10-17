from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from MyMenu.apps.menu.models import Dish, DishCategory
from MyMenu.apps.menu.serializers import DishSerializer, DishCategorySerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, ]


class DishCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    permission_classes = [IsAuthenticated, ]