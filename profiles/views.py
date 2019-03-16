from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# from .models import Guest
# from .forms import GuestForm
# from django.views import generic
#
# class GuestRegisterView(NextUrlMixin,RequestFormAttachMixin,generic.CreateView):
#     form_class = GuestForm
#     default_next = '/register/'
#     template_name = 'profiles/guest_register.html'
#
#     def get_success_url(self):
#         return self.get_next_url()
#
#     def form_invalid(self,form):
#         return redirect('profiles:register-guest')
#
# class AccountInfo(LoginRequiredMixin,generic.View):
#     def get(self,request):
#         return render(request,'profiles/account_auth_user_details.html')
