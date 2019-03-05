# from .models import Cart
# from django.db.models import Sum
#
# class CartTotal():
#     total = 0
#     def get_total(self):
#         cart = Cart.objects.get(user = request.user)
#         qty = cart.cart_items.aggregate(total=Sum('qty'))
#         if qty.get('total'):
#             return {'qty':total}
#         else:
#             total=0
#             return {"qty":total}
#         return self.total
#     def get_context_data(self,*args,**kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context[total] = self.get_total()
#         return context    
