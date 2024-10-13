
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def home_view(request):
    about = About.objects.first()  # Assuming you have a single "About" entry
    return render(request, 'home.html', {'about': about})