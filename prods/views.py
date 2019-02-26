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

def create_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('new cart made')
    return cart_obj


class AddItemToCart(View):
    def post(self,request,slug):
        # del request.session['cart_id']
        cart_id = request.session.get('cart_id',None)
        qs_cart = Cart.objects.filter(id=cart_id)
        if qs_cart.count() == 1:
            print('cart already exists')
            cart_obj = qs_cart.first()
        else:
            cart_obj = create_cart()
            request.session['cart_id']=cart_obj.id
        return redirect("/detail/{}/".format(slug))

class CartView(View):
    def get(self,request):
        return render(request,template_name = 'prods/cart.html')
