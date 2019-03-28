#profiles/forms.py

#django-paypal-1.0.0
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
#*************************************************************************
# <script type="text/javascript">
#     var proceed = $("#proceed");
#     var showAuth = $("#show-auth");
#     $(".go-on").on('click',function(e){
#         console.log("smb wants to login-signup=> but clicked");
#         e.preventDefault();
#         url = $(this).attr('href');
#         console.log("should be send to url",url);
#         $.ajax({
#             url:url,
#             type:"GET",
#             success:function(response){
#                 //show button Proceed
#                 console.log("success coming");
#                 showAuth.css('display','none');
#                 console.log("block auth but is disappeared")
#             },
#             error:function(err){
#                 console.log('error',err);
#             }
#         })//end ajax
#     })//end on click
# </script>
# <tr id="show-auth">
# <td></td><td></td><td></td><td></td><td></td><td></td>
# <td></td>
#     <td class="text-center">
#         <button class="btn btn-success">
#             <a class="go-on" href="{% url 'account_login' %}">Log In</a>
#         </button>
#     </td>
#     <td class="text-center">
#     <button class="btn btn-success">
#         <a class="go-on" href="{% url 'account_signup' %}">Sign Up</a>
#     </button>
#     </td>
# </tr>
# {% endif %}

# qs from palypal
# mc_gross=7.98
# &invoice=82&
# protection_eligibility=Eligible
# &payer_id=VFE8EA6D55VHA
# &payment_date=05%3A08%3A46+Mar+28%2C+2019+PDT
# &payment_status=Completed&charset=windows-1252
# &first_name=Tatjana
# &mc_fee=0.62
# &notify_version=3.9
# &custom=&payer_status=unverified
# &business=verkoper%40mail.com
# &quantity=1
# &verify_sign=A1fAO792yrQ6XB8vat4o8M7yIMCJAP2htM-HY-GzQGrqBpXgRy0j1KrY
# &payer_email=foofoo%40mail.com
# &txn_id=8NU45729BT610443A
# &payment_type=instant
# &last_name=Rietveldt
# &receiver_email=verkoper%40mail.com
# &payment_fee=&shipping_discount=0.00
# &receiver_id=KUL4LH5PFWQEE&insurance_amount=0.00
# &txn_type=web_accept&item_name=Order+ABCBMF&discount=0.00
# &mc_currency=EUR
# &item_number=
# &residence_country=NL
# &test_ipn=1
# &shipping_method=Default
# &transaction_subject=
# &payment_gross=
# &ipn_track_id=778575132ce6f
