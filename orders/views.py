from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,ListView   #FormView
from django.http import JsonResponse,HttpResponse
from prods.models import Cart
from .models import Order
from django.db.models import Sum
from profiles.models import BillingProfile
from profiles.forms import BillingProfileForm
# module for generation PDF
#from wkhtmltopdf.views import PDFTemplateView
#
# class MyPDF(PDFTemplateView):
#     filename = 'my_pdf.pdf'
#     template_name = 'orders/pdf.html'
#     cmd_options = {
#         'margin-top': 3,
#     }
def admin_order_detail(request,pk):
    order = get_object_or_404(Order, id=pk)
    cart = Cart.objects.get(order=order,accepted=True)
    cart_items = cart.cart_items.all()
    return render(request, 'admin/orders/order/detail.html',
            {'order': order,'cart':cart,'items':cart_items})

class ListOrder(ListView):
    """list of all pre-orders(based on accepted carts) but not paid yet"""
    model = Order
    context_object_name = "orders"
    template_name = 'orders/list_orders.html'

    def get_queryset(self):
        return  Order.objects.filter(cart__user = self.request.user,accepted=False).order_by('-date')

class OrderHistory(ListView):
    model = Order
    template_name = 'orders/order-history.html'

    def get_queryset(self):
        return Order.objects.filter(cart__user =            self.request.user,accepted=True,status='paid').order_by('-date')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['accepted_not_paid_yet_orders'] = Order.objects.filter(cart__user =            self.request.user,accepted=True).exclude(status='paid').order_by('-date')
        
        return context

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
class CreateOrder(View):
    """
    Display existing order or
    create a new one triggered by cart status => accepted False
    """
    # ? def get(in case user stops)
    def post(self,request):
        pk_cart = request.POST.get('pk','pk not found')
        print(pk_cart)
        cart = Cart.objects.get(id=pk_cart,accepted=False)
        # cart = Cart.objects.get(id=143,accepted=False)
        print(cart.id)
        order = Order.objects.create(cart=cart) # per default accepted=False)
        order.update_total()
        print("inside create order..created new one with id:",order.id)
        print("inside create order..and accepted :",order.accepted)
        cart.accepted = True
        cart.save()
        new_cart = Cart.objects.create(user=request.user)
        request.session["cart_id"] = new_cart.id
        return redirect('orders:list-orders')

class Checkout(View):
    def get(self,request):
        """make final order """
        pk=request.GET.get('pk')
        form = BillingProfileForm(
                instance=BillingProfile.objects.get(user__email=request.user.email)
                )
        order = get_object_or_404(Order,id=pk,accepted=False,cart__user=request.user)
        order.accepted = True
        order.save()
        request.session['order_id'] = order.id
        return render(request,'orders/checkout.html',{'form':form,'order':order})
