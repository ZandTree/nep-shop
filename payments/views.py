from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Payment(View):
    def get(self,request):
        return render(request,'payments/pay.html')
    def post(self,request):
        return render(request,'payments/pay.html')
