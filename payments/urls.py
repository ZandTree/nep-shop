from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('payment/',views.Payment.as_view(),name = 'pay'),
    path('done/',views.payment_done,name='done'),
    path('canceled/',views.payment_canceled,name='canceled'),


]
