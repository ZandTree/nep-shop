from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create-order/',views.CreateOrder.as_view(),name = 'create-order'),
    path('list-orders/',views.ListOrder.as_view(),name = 'list-orders'),
    path('delete-order/',views.DeleteOrder.as_view(),name = 'delete-order'),
    #path('final-order/',views.MakeFinalOrder.as_view(),name = 'final-order'),
    path('checkout/',views.Checkout.as_view(),name = 'checkout'),
    path('history/',views.OrderHistory.as_view(),name = 'history'),

]
