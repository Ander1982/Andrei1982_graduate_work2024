from django.shortcuts import render, redirect
from .models import Works
from django.utils import timezone

def works(request):
    works = Works.objects.all()
    return render(request, 'works/works.html', {'works': works})


def detail(request, works_id):
    return render(request, 'works/detail.html', {'works_id': works_id})

def delete(request,works_id):
    work = get_object_or_404(Works, pk=works_id)
    work.delete()
    return redirect('works')