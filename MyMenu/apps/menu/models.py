from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name,**kwargs):
        return name


class Dish(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(_('description'), max_length=300)
    image = models.ImageField(_('image'), upload_to='dishes/', null=True, blank=True, storage=OverwriteStorage())
    price = models.FloatField(_('price'), default=0)
    
    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')
