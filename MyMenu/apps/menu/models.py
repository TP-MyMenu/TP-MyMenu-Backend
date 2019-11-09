from django.db import models
from django.utils.translation import gettext_lazy as _


class DishCategory(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/categories', null=True, blank=True)

    class Meta:
        verbose_name = _('dish category')
        verbose_name_plural = _('dish categories')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/', null=True, blank=True)
    price = models.FloatField(_('price'), default=0)
    category = models.ForeignKey(DishCategory, verbose_name=_("dish category"), related_name='dishes',
                                 on_delete=models.CASCADE)
    suitable_for_celiacs = models.BooleanField(_('suitable for celiacs'), default=False)
    suitable_for_vegetarians = models.BooleanField(_('suitable for vegetarians'), default=False)

    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='drinks/', null=True, blank=True)
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
    dessert = models.ForeignKey(Dish, verbose_name=_('dessert'), on_delete=models.CASCADE, related_name='dessert')
    is_day_dish = models.BooleanField(_('is day dish'), default=False)
    price = models.IntegerField(_('price'), default=0)

    class Meta:
        verbose_name = _('day dish')
        verbose_name_plural = _('day dishes')


class Suggestion(models.Model):
    client_name = models.CharField(_('client name'), max_length=30, null=True, blank=True)
    suggestion = models.CharField(_('suggestion'), max_length=300)

    class Meta:
        verbose_name = _('suggestion')
        verbose_name_plural = _('suggestions')


class PaymentMethod(models.Model):
    method = models.CharField(_('method'), max_length=30)
    promotion = models.CharField(_('promotion'), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _('payment method')
        verbose_name_plural = _('payment methods')
