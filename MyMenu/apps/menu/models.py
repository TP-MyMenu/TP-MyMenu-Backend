from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, **kwargs):
        return name


class DishCategory(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/categories', null=True, blank=True, storage=OverwriteStorage())

    class Meta:
        verbose_name = _('dish category')
        verbose_name_plural = _('dish categories')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/', null=True, blank=True, storage=OverwriteStorage())
    price = models.FloatField(_('price'), default=0)
    category = models.ForeignKey(DishCategory, _("dish category"), related_name='dishes')

    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='drinks/', null=True, blank=True, storage=OverwriteStorage())
    price = models.FloatField(_('price'), default=0)

    class Meta:
        verbose_name = _('drink')
        verbose_name_plural = _('drinks')

    def __str__(self):
        return self.name


class DayDish(models.Model):
    main_dish = models.ForeignKey(Dish, verbose_name=_('main dish'), on_delete=models.CASCADE,
                                  related_name='day_dishes')
    garnish = models.ForeignKey(Dish, verbose_name=_('garnish'), on_delete=models.CASCADE, blank=True, null=True)
    drink = models.ForeignKey(Drink, verbose_name=_('drink'), on_delete=models.CASCADE, related_name='day_dishes')
    is_day_dish = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('day dish')
        verbose_name_plural = _('day dishes')

