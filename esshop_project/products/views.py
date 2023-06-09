from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'ESShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'ESShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

