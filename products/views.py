from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ a view to show all products and include sorting """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
