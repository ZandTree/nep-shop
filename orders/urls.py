from django.urls import path
from . import views

from wkhtmltopdf.views import PDFTemplateView

app_name = 'orders'
urlpatterns = [
    path('create-order/',views.CreateOrder.as_view(),name = 'create-order'),
    path('list-orders/',views.ListOrder.as_view(),name = 'list-orders'),
    path('delete-order/',views.DeleteOrder.as_view(),name = 'delete-order'),
    #path('final-order/',views.MakeFinalOrder.as_view(),name = 'final-order'),
    path('checkout/',views.Checkout.as_view(),name = 'checkout'),
    path('history/',views.OrderHistory.as_view(),name = 'history'),
    #path('generate/pdf/',views.generate_pdf,name='generate-pdf'),
    path('pdf/', PDFTemplateView.as_view(template_name='orders/pdf.html',
                                           filename='my_pdf.pdf'), name='pdf'),

]
