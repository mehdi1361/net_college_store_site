from django import template
from education.models import Course
from random import randint
register = template.Library()

@register.inclusion_tag("tags/single_course_tag.html")
def single_course(course):
     return {"course": course}