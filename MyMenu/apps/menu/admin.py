from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from MyMenu.apps.menu.models import Dish, DishCategory, DayDish
from MyMenu.apps.menu.service import DishService
from MyMenu.apps.menu.models import Drink


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    dish_service = DishService()
    list_display = ('name', 'description', 'price')
    list_filter = ('category', )

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


@admin.register(DayDish)
class DayDishAdmin(admin.ModelAdmin):
    dish_service = DishService()
    list_display = ('main_dish', 'garnish', 'drink', 'is_day_dish', 'custom_actions')
    readonly_fields = ('is_day_dish', )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [url(
            r'^(?P<day_dish_id>.+)/mark_as_day_dish/$',
            self.admin_site.admin_view(self.mark_as_day_dish),
            name='mark-as-day-dish',
        )]
        return custom_urls + urls

    def mark_as_day_dish(self, request, day_dish_id):
        self.dish_service.mark_as_day_dish(day_dish_id)
        return HttpResponseRedirect(reverse('admin:menu_daydish_changelist'))

    def custom_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">{}</a>',
            reverse('admin:mark-as-day-dish', args=[obj.pk]),
            _("Mark as day dish"))

    custom_actions.short_description = _("dish actions")


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
