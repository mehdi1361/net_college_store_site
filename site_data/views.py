from django.shortcuts import render
from .models import Slider, Category, CourseCategory
from education.models import Course
from random import randint
from education.models import Course

# Create your views here.


def index(request):
    course_categoris = CourseCategory.is_active.all()
    courses = Course.objects.filter(active=True).order_by('-id')[:6]
    return render(request, "index.html", {"courses": courses})

def list_course_category(request, course_category_id):
    course_category = CourseCategory.objects.get(pk=course_category_id)
    courses = Course.objects.filter(active=True, course_category=course_category)
    return render(request, "list_course_category.html", {
            "courses": courses, 
            "title": course_category.name
        })
    
    
def list_category(request, category_id):
    courses = Course.objects.filter(active=True, category__id=category_id)
    return render(request, "list_course_category.html", {
            "courses": courses, 
            "title": courses.first().category.name
        })

