from django.db import models
from django.utils.translation import gettext_lazy as _


# PERSON:
class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('First name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last name'))
    email = models.EmailField(verbose_name=_('Email'))

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
