from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from orders.models import Order
from django.dispatch import receiver

@receiver(valid_ipn_received)
def payment_notification(sender,**kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == "Completed": #ST_PP_COMPLETED:
        # payment successful
        order = get_object_or_404(Order,id=ipn_obj.invoice)
        if order.total == ipn.mc_gross:
        #mark the order as paid
            order.status = "paid"
            order.save()
    else:
        print("Hm....Smth went wrong")
