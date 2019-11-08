from django.shortcuts import render
from django.utils import timezone
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.filter(product_id=1)
    return render(request, 'product/product_list.html', {'products': products})
