from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from .models import *

class ProdList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'prods/index.html'

class ProdDetail(DetailView):
    model = Product
    context_object_name = 'product'

    


class CartDetail(View):
    def get(self,request):
        return render(request,template_name = 'prods/cart.html')
