from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    products = models.Product.objects.all()
    context = { 'products': products }

    return render(request, 'home.html', context)


def product_detail(request, pk):

    # product = models.Product.objects.get(pk=pk)
    product = get_object_or_404(models.Product, pk=pk)
    context = { 'product': product }

    return render(request, 'product_detail.html', context)