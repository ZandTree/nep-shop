from django.db import models
from prods.models import Cart
from bookstore.utils import make_unique_id
from django.db.models.signals import pre_save
from django.dispatch import receiver


ORDER_STATUS_CHOICES = (
    #('in db','to display')
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),

)

class Order(models.Model):
    order_id = models.CharField(max_length=120,blank=True) #AB3245
    cart = models.ForeignKey(Cart,related_name='order',on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True )
    shipping_total = models.DecimalField(default=5.00,max_digits=100,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    status = models.CharField(max_length=120,default="created",choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return "This is an order {}".format(self.order_id)

def order_id_presave_receiver(sender, instance,*args,**kwargs):
    if not instance.order_id: # if already created => no need to change
        instance.order_id = make_unique_id(instance)
        # don't call here save(!)
pre_save.connect(order_id_presave_receiver,sender=Order)
