from django.shortcuts import render
from .models import Slider, Category
from random import randint

# Create your views here.


def index(request):
    slider_count = randint(0, Slider.objects.count() - 1)
    slider = Slider.objects.all()[slider_count]
    
    categories = Category.objects.filter(active=True)
    
    return render(request, "index.html", {
        "slider": slider, 
        "categories": categories
    })