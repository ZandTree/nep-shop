from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                DeleteView,
                                View)
from .models import Product,Cart,CartItem,Category
from .forms import *
from django.contrib import messages
# class KillSession(View):
#     def get(self,request):
#         del request.session['cart_id']
#         return redirect('/')

class ProdList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'prods/index.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     # context['cart_id'] = self.request.session.get('cart',"not found")
    #     return context

class ProdDetail(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = CartItemForm()
        context['form'] = form
        return context

class AddItemToCart(View):
    def post(self,request,slug,pk):
        #del request.session['cart_id']
        cart = Cart.objects.new_or_get(request)
        prod = get_object_or_404(Product,id=pk)
        qty = request.POST.get('qty')
        if qty is not None and int(qty)>0:
            try:
                item = CartItem.objects.get(
                    cart = cart,
                    product = prod,
                    cart__accepted=False
                )
                item.qty += int(qty)
                item.save()
                messages.success(request, 'Qty changed.')

            except CartItem.DoesNotExist:
                item  = CartItem.objects.create(
                    cart = cart,
                    product = prod,
                    qty = int(qty)
                    )
                messages.success(request, 'New item added to your cart.')
        else:
            messages.error(request, 'Amount of product should be 1 or more.')

        return redirect("/detail/{}/".format(slug))


class CartItemsView(ListView):
    context_object_name = 'items'
    template_name = 'prods/cart.html'

    def get_queryset(self,*args,**kwargs):
        cart = Cart.objects.new_or_get(self.request)
        return cart.cart_items.all()

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        cart = Cart.objects.new_or_get(self.request)
        context['cart'] = cart
        one_item = cart.cart_items.all().last()
        context['prod'] = Product.objects.get(id=one_item.product_id)
        return context

class DeleteCartItem(View):
    def get(self,request,pk):
        cart_item = get_object_or_404(CartItem,id=pk,cart__user=request.user)
        cart_item.delete()
        messages.warning(request,'product deleted from your cart')
        return redirect('prods:cart')


class EditCartItem(View):
    """Edit item in cart"""
    def post(self, request, pk):
        quantity = request.POST.get("qty", None)
        if quantity:
            item = CartItem.objects.get(id=pk, cart__user=request.user)
            item.qty = int(quantity)
            item.save()
        return redirect("/cart/")
