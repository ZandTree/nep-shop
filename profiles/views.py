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
#
# class CheckOut(View):
#     """
#     collect user data for profile and final payment
#     # looks like cart display but + shipping payment
#     """
#     def post(self,request):
#         initial_data = {'email':request.user.email}
#         form = BillingProfileForm(initial=initial_data)
#         context = {'form':form}
#         return render(request,'orders/checkout.html',context)
    # form_class = BillingProfileForm
    # success_url = '/'
    # template_name = 'orders/checkout.html'
    # def get_initial(self):
    #     #initial= super().get_initial()
    #     # initial['email'] = self.request.user.email
    #     # return initial
    #     print({'email':self.request.user.email})
    #     return {'email':self.request.user.email}
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['email'] = self.request.user.email
    #     return kwargs
