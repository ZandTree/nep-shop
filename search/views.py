from django.shortcuts import render
from django.views.generic import ListView
from prods.models import Product
from django.db.models import Q


class SearchList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search/view_search.html'

    def get_queryset(self,*args,**kwargs):
        word = self.request.GET.get('q')
        if word is not None:
            return Product.objects.filter(Q(title__icontains=word)|Q(description__icontains=word))
        return Product.objects.none()
