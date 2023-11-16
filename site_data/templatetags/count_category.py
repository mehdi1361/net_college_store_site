from django import template

from site_data.models import Category

register = template.Library()

def count(args):
    return Category.objects.count()