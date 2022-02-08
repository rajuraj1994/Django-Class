from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Product
from .forms import *
from django.contrib import messages


# Create your views here.

def index(request):
    products = Product.objects.all()
    context ={
        'products': products
    }
    return render(request,'products/index.html',context)
    
     
def testFunc(request):
    return HttpResponse('this is just the test function')

def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'products/addproduct.html',{
                'form':form
            })
    context={
        'form':ProductForm
    }

    return render(request,'products/addproduct.html',context)

def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'products/addcategory.html',{
                'form':form
            })
    context={
        'form':CategoryForm
    }

    return render(request,'products/addcategory.html',context)