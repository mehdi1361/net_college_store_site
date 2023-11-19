from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from base.models import Base
from site_data.models import CourseCategory, Category

class Course(Base):
    COURSE_LEVEL = (
        ('begginer', 'begginer'), 
        ('intermediate', 'intermediate'), 
        ('advance', 'advance')
    )
    title = models.CharField(_("title"), max_length=50)
    intro = models.CharField(_("intro"), max_length=50)
    description = models.TextField(_("description"))
    price = models.PositiveIntegerField(_("price"), default=0)
    discount = models.PositiveIntegerField(_("discount"), default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    course_category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, null=True, blank=True
        )
    image = models.ImageField(_("image"), upload_to="course", null=True)
    level = models.CharField(_("level"), max_length=50, choices=COURSE_LEVEL, default='begginer')
    class Meta:
        db_table = "course"
        verbose_name = "courses"
        verbose_name_plural = "courses"
        
    @property
    def get_price_with_discount(self):
        return f'{self.discount:,}'