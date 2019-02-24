from django.db import models
import os
from django.http import Http404
from PIL import Image
from mptt.models import MPTTModel,TreeForeignKey
from .utils import make_unique_slug
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q


class Category(MPTTModel):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120,unique=True)
    parent = TreeForeignKey(
                "self",
                blank=True,
                null=True,
                on_delete=models.CASCADE,
                related_name='kids')
    class MPTTMeta:
        order_insertion_by=['name']
    class Meta:
        verbose_name = 'categories'
    def __str__(self):
        return  self.name

def upload_img_file(instance,filepath):
    """
    shorten filename and pack into folder with title + id
    let op: splitext returns already period='.ext'
    """
    filename = os.path.basename(filepath)         # 'abababa.jpeg'
    name,ext = os.path.splitext(filename)         # tuple ('abababa', '.jpeg')
    if len(name) > 5:
        name = name[:5]
    new_file_name = name + ext
    return os.path.join('image','prod_{0}','{1}').format(instance.id,new_file_name)

class ProductManager(models.Manager):
    def search(self,word):
        lookup = (Q(title__icontains=word)|
                    Q(description__icontains=word)|
                    Q(price__icontains=word)
                    )
        return Product.objects.filter(lookup).distinct()
    def for_sale(self):
        return Product.objects.filter(sale=True)

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120,blank=True,unique=True)
    price = models.DecimalField(max_digits=100000,decimal_places=2,default=1.99)
    description = models.TextField(default="")
    stock = models.BooleanField(default=True)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=upload_img_file,blank=True,null=True)
    categ = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

    objects = ProductManager() # not overriding but extending .objects()

    def __str__(self):
        return self.title
    def get_absolute_url(self,**kwargs):
        return reverse('prods:detail',kwargs={'slug':self.slug})

    @property
    def get_photo_url(self,*args,**kwargs):
        if self.photo:
            return "/media/{}".format(self.photo)
        else:
            return "/static/images/carrot.jpg/"
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            output_size = (253,380)
            img.thumbnail(output_size)
            img.save(self.photo.path)

class Cart(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)
    total = models.DecimalField(decimal_places=2,max_digits=10000000,editable=False)

    def save(self,*args,**kwargs):
        total = 0
        super().save(*args,**kwargs)

    def __str__(self):
        if self.user:
            return "cart id:{} user:{}".format(self.id,self.user.id)
        return  "cart id:{} anonymnus".format(self.id)

class Cartitem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_in_carts')
    qty = models.PositiveIntegerField(default=0,editable=False)
    sub_total = models.DecimalField(decimal_places=2,max_digits=10000000)

    def save(self,*args,**kwargs):
        """ generate price for each cart_item"""
        sub_total = self.product.price *self.qty
        super().save(*args,**kwargs)








@receiver(pre_save, sender=Product)
def product_presave_receiver(sender, instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = make_unique_slug(instance)
pre_save.connect(product_presave_receiver,sender=Product)
