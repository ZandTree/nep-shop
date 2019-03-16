from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# class Guest(models.Model):
#     email = models.EmailField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.email

class BillingProfile(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    create_account = models.BooleanField(default=False)

    def __str__(self):
        return self.email

def user_created_profile(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)
post_save.connect(user_created_profile,sender=User)
