from django.shortcuts import render
from .models import Works


def works(request):
    works = Works.objects.all()
    return render(request, 'works/works.html', {'works': works})


def detail(request, works_id):
    return render(request, 'works/detail.html', {'works_id': works_id})
