from django.db import models
from django.utils.translation import gettext_lazy as _


class Dish(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/', null=True, blank=True)
    price = models.FloatField(_('price'), default=0)

    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')
