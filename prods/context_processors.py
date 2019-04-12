from .models import Category,Cart

def list_categories(request):
    """
    List categories in sidebar
    """
    return {"cats":Category.objects.all()}


def count_items_cart(request):
    """
    Amount items for menubar
    """
    # print("now in context...looking for cart")
    # print("user is ",request.user)
    # print("preparing to call method .new_or_get...")
    cart = Cart.objects.new_or_get(request,accepted=False)
    # print("returned cart",cart)
    # print('cart is:',cart)
    # print('accepted is:',cart.accepted)
    qty = cart.get_sum_items_amount()
    return {"qty":qty}

#  LET OP : THERE IS A PROBLEM WITH ANO USER AND THIS context_processors
# solution: take .new_or_get(request)
