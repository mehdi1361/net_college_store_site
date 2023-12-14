from django import template
from site_data.models import CourseCategory, Category
register = template.Library()

@register.inclusion_tag("tags/menu.html")
def show_menu(*args):
     course_categories = CourseCategory.is_active.all()
     categorries = Category.is_active.all()
     return {
         "course_categories": course_categories, 
         "categories": categorries
    }