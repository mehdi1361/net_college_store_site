from django.db import models
from base.models import Base
# Create your models here.
from django.utils.translation import ugettext_lazy as _

class Slider(Base):
    title = models.CharField(_("title"), max_length=50)
    text = models.CharField(_("text"), max_length=50)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to="slider")

    class Meta:
        verbose_name = _("slider")
        verbose_name_plural = _("sliders")

    def __str__(self):
        return self.title


class Category(Base):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to="category")
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name
