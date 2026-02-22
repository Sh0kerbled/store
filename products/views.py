from django.shortcuts import render, HttpResponse
from products.models import Product, ProductCategory

def index(req):
    context = {
        'title': 'Store',
        'is_promotion': True
    }
    return render(req, "products/index.html", context)

def products(req):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(req, "products/products.html", context)

def not_found(req, exception):
    return render(req, "products/404.html", status=404)