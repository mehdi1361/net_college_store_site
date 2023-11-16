from django.shortcuts import render
from .models import Slider, Category, CourseCategory
from random import randint

# Create your views here.


def index(request):
    course_categoris = CourseCategory.is_active.all()
    
    return render(request, "index.html")