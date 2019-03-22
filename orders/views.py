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
    # LoginRequiredMixin????
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


#
#     def post(self,request):
#         cart = get_object_or_404(Cart,id=request.POST.get('pk'))
#         total = cart.cart_items.aggregate(total=Sum('sub_total'))
#         summa = total.get('total')
        # here += shipping_total
        # let op *1001 ...order = Order.objects.create(cart=cart,accepted=False,total=summa) # per default accepted=False)
        # cart.accepted = True
        # cart.save()
        # new_cart = Cart.objects.create(user=request.user)
        #return render(request,'orders/create_order.html',{'cart':cart,'summa':summa,'order':order})
#
class ListOrder(ListView):
    model = Order
    template_name = 'orders/list_orders.html'
