from django import forms
from profiles.models import BillingProfile

class BillingProfileForm(forms.ModelForm):
    #email = forms.EmailField(initial={{user.email}})
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
        #self.fields['email'].label="Your email"
        # self.email = kwargs.pop("email")
        # print(self.email)
        # self.fields['email']=kwargs.pop("email")


    class Meta:
        model = BillingProfile
        fields = ['email','create_account']
