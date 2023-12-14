from django import  template
from site_data.models import Category
register = template.Library()


@register.inclusion_tag("tags/category.html")
def show_category(*args):
    categories = Category.is_active.all()
    return {"categories": categories}
    