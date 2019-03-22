from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,ListView   #FormView
from prods.models import Cart
from .models import Order
from django.db.models import Sum
from profiles.models import BillingProfile
from .forms import BillingProfileForm

class CreateOrder(View):
    """
    Display existing order or
    create a new one triggered by cart status => accepted False
    """
    def post(self,request):
        pk_cart = request.POST.get('pk','pk not found')
        cart = Cart.objects.get(id=pk_cart,accepted=False)
        order = Order.objects.create(cart=cart) # per default accepted=False)
        order.update_total()
        cart.accepted = True
        cart.save()
        new_cart = Cart.objects.create(user=request.user)
        request.session["cart_id"] = new_cart.id
        return redirect('orders:list-orders')

class ListOrder(ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'orders/list_orders.html'

    def get_queryset(self):
        return  Order.objects.filter(accepted=False)
