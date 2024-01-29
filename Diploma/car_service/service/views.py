from django.shortcuts import render
from .models import Service


def index(request):
    projects = Service.objects.all()
    return render(request, 'service/index.html', {'projects': projects})