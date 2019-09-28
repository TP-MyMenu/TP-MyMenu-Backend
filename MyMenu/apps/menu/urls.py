from django.urls import path, include
from rest_framework import routers

from MyMenu.apps.menu import views

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
