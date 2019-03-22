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
