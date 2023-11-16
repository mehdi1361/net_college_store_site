from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Base(models.Model):
    created_date = models.DateTimeField(_("created_date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("updated_date"), auto_now=False, auto_now_add=False)
    active = models.BooleanField(_("active"), default=True)

    class Meta:
        abstract = True

