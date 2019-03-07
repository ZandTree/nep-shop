from django.urls import path
from . import views

app_name = 'prods'
urlpatterns = [
    path('',views.ProdList.as_view(),name = 'home'),
    #path('kill-session',views.KillSession.as_view(), name='kill'),
    path('detail/<slug:slug>/',views.ProdDetail.as_view(),name = 'detail'),
    path('cart/',views.CartItemsView.as_view(),name = 'cart'),
    path('delete-cart-item/<int:pk>/',views.DeleteCartItem.as_view(),name = 'delete-cart-item'),
    path('edit-cart-items/<int:pk>/',views.EditCart.as_view(),name = 'edit-cart-items'),
    path('add-to-cart/<slug:slug>/<int:pk>/',views.AddItemToCart.as_view(),name = 'add-to-cart'),


]
