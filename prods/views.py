from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                View)
from .models import Product,Cart,CartItem,Category
from .forms import *

class ProdList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'prods/index.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        # context['cart_id'] = self.request.session.get('cart',"not found")
        return context

class ProdDetail(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = CartItemForm()
        context['form'] = form
        return context

class AddItemToCart(View):
    def post(self,request,slug):
        #del request.session['cart_id']
        cart,new_obj = Cart.objects.new_or_get(request)
        return redirect("/detail/{}/".format(slug))


class CartView(View):
    def get(self,request):
        return render(request,template_name = 'prods/cart.html')
