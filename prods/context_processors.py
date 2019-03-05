from .models import Cart
from django.db.models import Sum

def count_items_cart(request):
    """
    Amount items for menubar
    """
    cart = Cart.objects.get(user = request.user)
    qty = cart.cart_items.aggregate(total=Sum('qty'))
    total = qty.get('total')
    if total:
        return {'qty':total}
    else:
        total = 0
        return {"qty":total}
