from django.urls import path, include
from rest_framework import routers

from MyMenu.apps.menu import views

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet)
router.register(r'drinks', views.DrinkViewSet)
router.register(r'day_dish', views.DayDishViewSet)
router.register(r'suggestion', views.SuggestionViewSet)
router.register(r'payment_method', views.PaymentMethodViewSet)
router.register(r'dish_category', views.DishCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
