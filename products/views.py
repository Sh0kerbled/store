from django.shortcuts import render, HttpResponse

def index(req):
    return render(req, "products/index.html")

def products(req):
    return render(req, "products/products.html")