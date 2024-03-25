from django.shortcuts import render
from . import models

# Create your views here.

def products_main(request):
    top_sales = models.Product.objects.order_by('-sale_count').values_list('sale_count',flat=True).distinct()
    top_products = models.Product.objects.order_by('-sale_count').filter(sale_count__in=top_sales[:6])
    context = {
        'top_products' : top_products
    }
    return render(request,'event/products-main-page.html',context)

def all_products(request):
    product_list = models.Product.objects.all()
    context = {
        'product_list' : product_list
    }
    return render(request,'event/product-list.html',context)