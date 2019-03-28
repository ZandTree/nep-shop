from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
#from django.core.urlresolvers import reverse nvt in dajngo >=2
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import View
from orders.models import Order
from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

class Payment(View):
    def get(self,request):
        order_id = request.session.get('order_id')
        print("order_id calling from session",order_id)
        order = get_object_or_404(Order,id=order_id)
        host = request.get_host()
        print(host)
        paypal_dict = {
            'business':settings.PAYPAL_RECEIVER_EMAIL,
            'amount' :'%.2f'%order.total.quantize(Decimal('.01')),
            'item_name':'Order {}'.format(order.order_id),
            'invoice':str(order.id),#id will be used later in signal
            'currency_code':'EUR', #USD',
            'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url':'http://{}{}'.format(host,reverse('payments:done')),
            'cancel_return':'http://{}{}'.format(host,reverse('payments:canceled'))
        }
        form = PayPalPaymentsForm(initial=paypal_dict)

        return render(request,'payments/process.html',{'order':order,'form':form})

@csrf_exempt
def payment_done(request):
 return render(request, 'payments/done.html')
@csrf_exempt
def payment_canceled(request):
 return render(request, 'payments/canceled.html')
