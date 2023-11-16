from django.shortcuts import render
from .models import Slider, Category, CourseCategory
from random import randint

# Create your views here.


def index(request):
    slider_count = randint(0, Slider.objects.count() - 1)
    slider = Slider.objects.all()[slider_count]
    course_categoris = CourseCategory.is_active.all()
    
    categories = Category.is_active.all()
    
    return render(request, "index.html", {
        "slider": slider, 
        "categories": categories, 
        "course_categories": course_categoris
    })