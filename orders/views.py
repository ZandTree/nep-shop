from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from prods.models import Cart
from .models import Order
from django.db.models import Sum
from profiles.models import BillingProfile

class CheckOut(View):
    def post(self,request):
        next_url = "orders:checkout"
        # next_ = request.GET.get("next")
        # next_post = request.POST.get("next")
        # redirect_path = next_  #or next_post or None
        cart = Cart.objects.new_or_get(request)
        # order_object = None
        # if cart.accepted == True or cart.cart_items.count()==0:
        #     #print("Your cart is empty or #already ***")
        #     return redirect("/")
        # else:
        #     order_object,new_order_obj = Order.objects.get_or_create(cart=cart)
        #     cart.accepted = True
        #     cart.save()
        #     new_cart =Cart.objects.create(user=request.user,accepted=False)
        # user = request.user
        # billing_profile = None
        # if user.is_authenticated:
        #     billing_profile,billing_profile_created = BillingProfile.objects.get_or_create(user=user,email=user.email)
        # context = {
        #     "object":order_object,
        #     "billing_profile":billing_profile,
        #     "next_url":next_url
        # }
        context = {'cart':cart}
        return render(request,'orders/checkout.html',context)



#
# class CreateOrder(View):
#     """
#     Display existing order or
#     create a new one triggered by cart status => accepted False
#     """
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
#
