from django.shortcuts import render
from django.views.generic import ListView
from prods.models import Product
from django.db.models import Q


class SearchList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search/view_search.html'
    paginate_by = 6

    def get_queryset(self,*args,**kwargs):
        word = self.request.GET.get('q')
        if word is not None:
            return Product.objects.search(word)
        return Product.objects.none()

class SaleList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search/view_search.html'

    def get_queryset(self,*args,**kwargs):
        return Product.objects.for_sale()
