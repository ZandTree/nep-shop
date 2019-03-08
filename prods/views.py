from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import JsonResponse
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                DeleteView,
                                View)
from .models import Product,Cart,CartItem,Category
from .forms import *
from django.contrib import messages
from django.db.models import Sum
# class KillSession(View):
#     def get(self,request):
#         del request.session['cart_id']
#         return redirect('/')

class ProdList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'prods/index.html'


class ProdDetail(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = CartItemForm()
        context['form'] = form
        return context

class AddItemToCart(View):
    def get(self,request,slug,pk):
        #del request.session['cart_id']
        cart = Cart.objects.new_or_get(request)
        prod = get_object_or_404(Product,id=pk)
        flag = False
        try:
            item = CartItem.objects.get(
                cart = cart,
                product = prod,
                cart__accepted=False
            )
            flag = True
            messages.error(request, 'Product is already in your cart.')
        except CartItem.DoesNotExist:
            item  = CartItem.objects.create(
                cart = cart,
                product = prod,
                qty = 1
                )
            messages.success(request, 'New item added to your cart.')
        if request.is_ajax():
            total_qty = cart.cart_items.aggregate(total=Sum('qty'))
            num_items = total_qty.get('total')
            return JsonResponse({"flag":flag,"numItems":num_items})
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
        total_price = cart.cart_items.aggregate(total_price=Sum('sub_total'))
        price = total_price.get('total_price')
        context['price'] = price
        # что-то непонятное
        one_item = cart.cart_items.all().last()
        # if one_item:
        #     context['prod'] = Product.objects.get(id=one_item.product_id)
        return context


class EditCart(View):
    def post(self,request,pk):
        #del request.session['cart_id']
        cart = Cart.objects.new_or_get(request)
        cart_item = get_object_or_404(CartItem,id=pk)
        #print(cart_item.product_id)
        prod= Product.objects.get(id=cart_item.product_id)
        qty = request.POST.get('qty')
        if qty is not None and int(qty)>0:
            item = CartItem.objects.get(
                cart = cart,
                product = prod,
                cart__accepted=False
            )
            item.qty = int(qty)
            item.save()
            messages.success(request, 'Qty changed.')

        else:
            messages.error(request, 'Amount of product should be 1 or more.')
        # qty = cart.cart_items.aggregate(total=Sum('qty'))
        # total = qty.get('total',0)
        # return JsonResponse({'qty':total})

        return redirect('prods:cart')


class DeleteCartItem(View):
    def get(self,request,pk):
        cart_item = get_object_or_404(CartItem,id=pk)
        cart_item.delete()
        messages.warning(request,'product deleted from your cart')
        return redirect('prods:cart')
