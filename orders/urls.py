from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('proceed-checkout/',views.CreateOrder.as_view(),name = 'create-order'),

]
