from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import Product
from .forms import ListForm
import base64
from django.db.models import Q
import operator
from functools import reduce
#import range


# Create your views here.

#def product_list(request):
#    products = Product.objects.all()
#    return render(request, 'product/product_list.html', {'products': products})

def product_list(request):
  
    products = Product.objects.all()

    query = request.GET.get('q')
    if query:
        query_list = query.split()
        products = products.filter(reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)))# |
              #  reduce(operator.and_,
              #         (Q(product_description__icontains=q) for q in query_list)))
        print(products)
    products_arr = []
    #for i in range(1,len(products)+1):
    for product in products:
       # product = Product.objects.get(product_id=i)
        product_obj = {
            'ID' : product.ID,
            'Title' : product.Title,
            'Description' : product.Description,
            'Category' : product.Category,
            'Quantity' : product.Quantity,
            'Size' : product.Size,
            'Image' : base64.b64encode(product.Image).decode() if product.Image is not None else '',
            'Brand' : product.Brand,
            'Color' : product.Color,
            'Condition' : product.Condition,    
            'Seller' : product.Seller,
            'Original_Price' : product.Original_Price,
            'Listing_Price' :  product.Listing_Price
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
  