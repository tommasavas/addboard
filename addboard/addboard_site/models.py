from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100, db_index=True)
    priority = models.IntegerField(_('priority'), default = 0, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('-priority', 'name')

