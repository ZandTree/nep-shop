#profiles/forms.py
from django import forms
#
# class GuestForm(forms.ModelForm):
#     class Meta:
#         fields = ['email',]
#
#     def __init__(self,request,*args,**kwargs):
#         self.request = request
#         # now you should provide param = request each time you call GuestForm
#         super().__init__(*args,**kwargs)
#
#     def save(self,commit=True):
#         #save the provided pws in hash
#         obj = super().save(commit=False)
#         if commit:
#             obj.save()
#             request = self.request
#             request.session['guest_email_id']=obj.id
#         return obj

    # these help to avoid form_valid in views
    # def form.valif(self,form):
    #     request = self.request
    #     email = form.cleaned_data.get("email")
    #     new_guest_email = Guest.objects.create(email=email)
    #     return redirect(self.get_next_url())
