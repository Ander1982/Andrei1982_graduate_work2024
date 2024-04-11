from django.shortcuts import render, redirect
from .models import Works, ProductCategory, Product
from django.utils import timezone


# def works(request):
#     works = Works.objects.all()
#     return render(request, 'works/works.html', {'works': works})


# def detail(request):
#     product = get_object_or_404(Product, pk=category_id)
#     return render(request, 'works/detail.html', {'product': product})


#
#
# def delete(request, works_id):
#     work = get_object_or_404(Works, pk=works_id)
#     work.delete()
#     return redirect('works')


def products(request):
    context = {
        'title': 'Каталог шин',
        'categories': ProductCategory.objects.all(),

    }

    return render(request, 'works/works.html', context)


def product(request, category_id):
    context = {
        'products': Product.objects.filter(category_id=category_id)
    }
    return render(request, 'works/detail.html', context)
