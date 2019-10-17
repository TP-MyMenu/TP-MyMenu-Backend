from MyMenu.apps.menu.repository import DishRepository


class DishService:
    dish_repository = DishRepository()

    def mark_as_day_dish(self, dish_id):
        self.dish_repository.day_dish().update(is_day_dish=False)
        self.dish_repository.get(dish_id).update(is_day_dish=True)
