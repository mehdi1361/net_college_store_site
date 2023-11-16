from django import template
from site_data.models import CourseCategory
register = template.Library()

@register.inclusion_tag("tags/course_categories.html")
def show_course_category(*args):
     course_categories = CourseCategory.is_active.all()
     return {"course_categories": course_categories}