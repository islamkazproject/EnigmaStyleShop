from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Product, ProductCategory, Basket


def index(request):
    context = {
        'title': 'ESShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'ESShop - Каталог',
               'categories': ProductCategory.objects.all() }

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    query = request.GET.get('q')
    if query is not None:
        finded_products = Product.objects.filter(name__icontains=query).order_by('-id')
        paginator = Paginator(finded_products, 3)
    else:
        paginator = Paginator(products, 3)

    products_paginator = paginator.page(page)
    context.update({'products': products_paginator, 'query': query})
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, id):
    current_page = request.META.get('HTTP_REFERER')
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(current_page)
