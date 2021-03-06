from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import Product
from .forms import ListForm
import base64
from django.db.models import Q
import operator
from functools import reduce
import datetime
from django.shortcuts import redirect
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
                       (Q(Title__icontains=q) for q in query_list)))# |
              #  reduce(operator.and_,
              #         (Q(product_description__icontains=q) for q in query_list)))
        #print(products)
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
            'Image' :product.Image,
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
    quant = product.Quantity
    arr = []
    for i in range(quant):
        arr.append(i+1)

    product.Quantity = arr
    return render(request, 'product/product_detail.html', {'product': product})

def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.Seller = request.user
            product.Posted_Date = datetime.datetime.now()
            product.Image = request.FILES['Image']
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ListForm()
    return render(request,'product/list_product.html',{'form':form})

def about_us(request):
    return render(request, 'product/About_Us.html')

def how_it_works(request):
    return render(request, 'product/how_it_works.html')
  
def checkout(request, p):
    return render(request, 'product/Checkout.html', {'p':p})