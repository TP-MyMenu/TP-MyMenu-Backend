from django.contrib import admin

from MyMenu.apps.menu.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
