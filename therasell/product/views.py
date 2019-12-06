from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import Product
from .forms import ListForm
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
          'product_id' : product.product_id,
          'title': product.title,
          'product_description': product.product_description,
          'Image' : base64.b64encode(product.Image).decode() if product.Image is not None else '',
          'Price' : '100'
        }
        products_arr.append(product_obj)
    return render(request, 'product/product_list.html', {'products': products_arr})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

def list_new(request):
    form=ListForm()
    return render(request,'product/list_product.html',{'form':form})

def about_us(request):
    return render(request, 'product/About_Us.html')

def how_it_works(request):
    return render(request, 'product/how_it_works.html')
  