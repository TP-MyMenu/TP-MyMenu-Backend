from django.db.models.query import EmptyQuerySet

from MyMenu.apps.menu.models import Dish


class DishRepository:
    def day_dish(self):
        return Dish.objects.filter(is_day_dish=True)

    def get(self, dish_id):
        return Dish.objects.filter(id=dish_id)
