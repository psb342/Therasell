from django.shortcuts import render
#from django.utils import timezone
from .models import Product
import base64
#import range


# Create your views here.

#def product_list(request):
#    products = Product.objects.all()
#    return render(request, 'product/product_list.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    products_arr = []
    for i in range(1,len(products)+1):
        product = Product.objects.get(product_id=i)
        product_obj = {
          'title': product.title,
          'product_description': product.product_description,
          'Image' : base64.b64encode(product.Image).decode(),
          'Price' : '100'
        }
        products_arr.append(product_obj)
    return render(request, 'product/product_list.html', {'products': products_arr})
