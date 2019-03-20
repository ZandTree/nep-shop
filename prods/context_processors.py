from .models import Cart
from django.db.models import Sum

def count_items_cart(request):
    """
    Amount items for menubar
    """
    # print("now in context...looking for cart")
    # print("user is ",request.user)
    # print("preparing to call method .new_or_get...")
    cart = Cart.objects.new_or_get(request,accepted=False)
    #print("returned cart",cart)
    # print('cart is:',cart)
    # print('accepted is:',cart.accepted)
    qty = cart.cart_items.aggregate(total=Sum('qty'))
    total = qty.get('total')
    # print('total',total)
    if total:
        return {'qty':total}
    else:
        total = 0
        return {"qty":total}

#  LET OP : THERE IS A PROBLEM WITH ANO USER AND THIS context_processors
# solution: take .new_or_get(request)
