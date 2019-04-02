from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.views.generic import View,TemplateView
from orders.models import Order
from django.shortcuts import get_object_or_404
#from django.core.urlresolvers import reverse nvt in dajngo >=2
from paypal.standard.forms import PayPalPaymentsForm
#stripe
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
#stripe
import stripe


class PayPalPayment(View):
    """Payment through PayPay"""
    def get(self,request):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order,id=order_id)
        host = request.get_host()
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
        return render(request,'payments/process.html', {'order':order,'form':form})

@csrf_exempt
def payment_done(request):
 return render(request, 'payments/done.html')
@csrf_exempt
def payment_canceled(request):
 return render(request, 'payments/canceled.html')

class StripePayment(TemplateView):
    """ To start payment through Stripe payment system"""
    template_name = 'payments/start_stripe.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

class StripeCharge(TemplateView):
    def post(self,request):
        print(request.POST)
        stripe.api_key = settings.SRTIPE_SECRET_KEY
        # customer = stripe.Customer.create(
        #     email = request.user.email,
        #     source = request.POST['stripeToken']
        # )
        charge  = stripe.Charge.create(
            #customer = customer.id,
            amount = 500,
            currency="usd",
            description='Pay Now',
            # using unique token for this user from Stripe
            source = request.POST['stripeToken']

        )
        return render(request,'payments/charge_stripe.html')
"""
<QueryDict:
 {'csrfmiddlewaretoken': ['297JSh5EeiN0JwFwz1fXuU0zoBEhkZ0K5qn7Kge25EiqpQvOg1aPodMglpVW6q0M'], 'stripeEmail': ['wally@mail.com'], 'stripeTokenType': ['card'], 'stripeToken': ['tok_1EKtjpCB9jcWPPd3xX7ofmrb']}>
"""
