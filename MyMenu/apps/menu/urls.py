from django.urls import path, include
from rest_framework import routers

from MyMenu.apps.menu import views

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet)
router.register(r'drinks', views.DrinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
