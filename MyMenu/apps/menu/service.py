from MyMenu.apps.menu.models import DayDish


class DishService:
    def mark_as_day_dish(self, day_dish_id):
        current = DayDish.objects.filter(is_day_dish=True)
        if current:
            current.update(is_day_dish=False)
        DayDish.objects.filter(id=day_dish_id).update(is_day_dish=True)
