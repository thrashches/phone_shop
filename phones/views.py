from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = 'id'

    if 'sort' in request.GET:
        if request.GET.get('sort') == 'name':
            # По названию
            sort = 'name'

        elif request.GET.get('sort') == 'min_price':
            # Сначала дешевые
            sort = 'price'

        elif request.GET.get('sort') == 'max_price':
            # Сначала дорогие
            sort = '-price'

    phones = Phone.objects.all().order_by(sort)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
