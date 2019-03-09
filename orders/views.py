from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from prods.models import Cart
from .models import Order
from django.db.models import Sum



# Create your views here.

class CreateOrder(View):
    """
    Display existing order or
    create a new one triggered by cart status => accepted False
    """
    def post(self,request):
        cart = get_object_or_404(Cart,id=request.POST.get('pk'))
        total = cart.cart_items.aggregate(total=Sum('sub_total'))
        summa = total.get('total')
        order = Order.objects.create(cart=cart,accepted=False,total=summa) # per default accepted=False)
        # cart.accepted = True
        # cart.save()
        # new_cart = Cart.objects.create(user=request.user)
        return render(request,'orders/create_order.html',{'cart':cart,'summa':summa})
#
#
