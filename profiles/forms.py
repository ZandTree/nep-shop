from django import forms
from profiles.models import BillingProfile

class BillingProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    district = forms.CharField(required=False)
    #email = forms.EmailField(initial={{user.email}})
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label="Your email"
        # self.email = kwargs.pop("email")
        # print(self.email)
        # self.fields['email']=kwargs.pop("email")
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].help_text = 'Not required'
        self.fields['district'].label = 'District/Provintie/Regio'
        self.fields['district'].help_text = 'Not required'


    class Meta:
        model = BillingProfile
        fields = ['last_name','first_name',
                'email','country','state',
                'city','district','street',
                'house_number','postcode','phone'
                ]
        widgets = {'postcode':forms.TextInput(attrs={'placeholder':"for example:1234AB"}),
                'phone':forms.TextInput(attrs={'placeholder':"for example:06-1234567"})
            }
