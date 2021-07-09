from django.shortcuts import render, HttpResponse
from .models import Producto


# Create your views here.

# def inicio(request):
#     return render(request, 'index.html')

def index(request):
    products = Producto.objects.all().order_by('-id')[:3]
    print(products)
    context = {'products' : products}
    return render(request, 'index.html', context)