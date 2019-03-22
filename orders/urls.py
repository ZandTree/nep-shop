from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create-order/',views.CreateOrder.as_view(),name = 'create-order'),
    path('list-orders/',views.ListOrder.as_view(),name = 'list-orders'),
    #path('checkout/',views.CheckOut.as_view(),name = 'checkout'),

]
