from .models import Cart
from django.db.models import Sum

# def count_items_cart(request):
#     """
#     Amount of items in the cart
#     """
#     cart = Cart.objects.get(user = request.user)
#     amount = cart.cart_items.all() #count()
#     qty = 0
#     for item in amount:
#         qty += item.qty
#     return {"menu_cart_items":qty}

def count_items_cart(request):
    """
    Amount of items in the cart
    """
    cart = Cart.objects.get(user = request.user)
    qty = cart.cart_items.aggregate(total=Sum('qty'))
    return {"qty":qty}
