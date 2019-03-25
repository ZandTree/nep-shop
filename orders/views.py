from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,ListView   #FormView
from django.http import JsonResponse
from prods.models import Cart
from .models import Order
from django.db.models import Sum
from profiles.models import BillingProfile
from profiles.forms import BillingProfileForm

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
    """list of all pre-orders(based on accepted carts) but not paid yet"""
    model = Order
    context_object_name = "orders"
    template_name = 'orders/list_orders.html'
    ordering = ['-date']

    def get_queryset(self):
        return  Order.objects.filter(cart__user = self.request.user,accepted=False)

class DeleteOrder(View):
    """user can remove pre-order from list of orders"""
    def post(self,request):
        pk = request.POST.get('pk')
        order = get_object_or_404(Order,id=pk,accepted=False)
        cart = get_object_or_404(Cart,id=order.cart.id,accepted=True)
        order.delete()
        cart.delete()
        return redirect('orders:list-orders')
#
class MakeFinalOrder(View):
    def post(self,request):
        """make final order and bind its id to session"""
        pk=request.POST.get('pk')
        final_order = get_object_or_404(Order,id=pk,accepted=False)
        final_order.accepted = True
        final_order.save()
        print(final_order)
        request.session["order_id"] = final_order.id
        return redirect('orders:checkout')

class Checkout(View):
    def get(self,request):
        """render billing form """
        order_id = request.session.get('order_id',None)
        if order_id is not None:
            order_to_pay = get_object_or_404(Order,id=order_id,accepted=True)
        form = BillingProfileForm(
                instance=BillingProfile.objects.get(user__email=request.user.email)
                )
        return render(request,'orders/checkout.html',{'form':form,'order':order_to_pay})

    # def post(self,request):
    #     """ save filled billing form  """
    #     form = BillingProfileForm(request.POST)

        # if form.is_valid():
        #     print("nice form")
        # else:
        #     print("Oh-Oh")
        # if form.is_valid():
        #     print("form is valid")
        #     del request.session['order_id']
        #     print('deleting session')
        #     obj = form.save(commit=False)
        #     print('updated form data')
        #     obj.user = request.user
        #     obj.save()
        #     print('profile should be saved?')
        # else:
        #     print('smth wrong with your form?')
        #return redirect("/")
class OrderHistory(ListView):
    model = Order
    template_name = 'orders/order-history.html'
    ordering = ['-date']

    def get_queryset(self):
        return Order.objects.filter(cart__user = self.request.user,accepted=True)
