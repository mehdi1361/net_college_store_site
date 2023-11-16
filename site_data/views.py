from django.shortcuts import render
from .models import Slider, Category

# Create your views here.


def index(request):
    slider = Slider.objects.first()
    
    return render(request, "index.html", {
    })