from django.db import models
from django.db.models.query import QuerySet
from base.models import Base
# Create your models here.
from django.utils.translation import ugettext_lazy as _

class ActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(active=True)

class DeActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().exclude(active=True)
    
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
    
    objects = models.Manager()
    is_active = ActiveManager()
    not_active = DeActiveManager()
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

class CourseCategory(Base):
    colors = (
        ("cat-1", "cat-1"),
        ("cat-2", "cat-2"),
        ("cat-3", "cat-3"),
        ("cat-4", "cat-4"),
        ("cat-10", "cat-10"),
        ("cat-6", "cat-6"),
        ("cat-7", "cat-7"),
        ("cat-8", "cat-8"),
        ("cat-9", "cat-9"),
    )
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="course_category")
    color = models.CharField(_("COLOR"), max_length=100, choices=colors)
    
    objects = models.Manager()
    is_active = ActiveManager()
    not_active = DeActiveManager()

    def __str__(self):
        return self.name
