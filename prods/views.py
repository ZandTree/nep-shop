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

    # def get_object(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     obj = Product.objects.get_prod_byId(pk)
    #     if obj is None:
    #         raise Http404("Oups,This product is not found")
    #     return obj



class CartDetail(View):
    def get(self,request):
        return render(request,template_name = 'prods/cart.html')
