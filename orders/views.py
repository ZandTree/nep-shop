from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class CreateOrder(View):
    """
    Display existing order or
    create a new one triggered by cart status => accepted False
    """
    def post(self,request):
        return render(request,'prods/create_order.html')
#     def post(self,request):
#         cart = Cart.objects.get(id=request.POST.get('pk'),user=request.user)
#         order = Order.objects.create(cart=cart) # per default accepted=False)
#         cart.accepted = True
#         cart.save()
#         new_cart = Cart.objects.create(user=request.user)
#         return redirect('shop:display_order')
