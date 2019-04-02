from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('payment_paypal/',views.PayPalPayment.as_view(),name = 'pay'),
    path('payment_stripe/',views.StripePayment.as_view(),name = 'start_stripe'),
    path('stripe_charge/',views.StripeCharge.as_view(),name="stripe_charge"),
    path('done/',views.payment_done,name='done'),
    path('canceled/',views.payment_canceled,name='canceled'),


]
