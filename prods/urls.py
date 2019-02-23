from django.urls import path
from . import views

app_name = 'prods'
urlpatterns = [
    path('',views.ProdList.as_view(),name = 'home'),
    path('detail/<slug:slug>/',views.ProdDetail.as_view(),name = 'detail'),
    path('cart/',views.CartDetail.as_view(),name = 'cart-detail'),

]
