from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from MyMenu.apps.menu.models import Dish
from MyMenu.apps.menu.serializers import DishSerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, ]
