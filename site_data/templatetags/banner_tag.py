from django import template
from site_data.models import Slider
from random import randint
register = template.Library()

@register.inclusion_tag("tags/banner.html")
def show_slider(*args):
     slider_count = randint(0, Slider.objects.count() - 1)
     slider = Slider.objects.all()[slider_count]
     return {"slider": slider}