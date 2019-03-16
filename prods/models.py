from django.db import models
import os
from django.http import Http404
from PIL import Image
from mptt.models import MPTTModel,TreeForeignKey
from bookstore.utils import make_unique_slug
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db.models import Sum


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
                    Q(price__icontains=word)|
                    Q(tags__title__icontains=word)
                    # without related_name use just tag_title,tag_sluf (through the field)
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

class CartManager(models.Manager):
    def new_or_get(self,request,accepted=False):
        #del request.session['cart_id']
        cart_id = request.session.get('cart_id',None)
        qs = self.get_queryset().filter(id=cart_id,accepted=False)
        if qs.count() == 1:
            #уже есть
            cart_obj = qs.first()
            print('model manager msg: this cart belongs to:',cart_obj.user)
            if request.user.is_authenticated and cart_obj.user is None:
                # taking previous cart auth user
                prev_cart = get_object_or_404(Cart,user=request.user,accepted=False)
                prev_cart.delete() # prev cart auth user will be deleted
                cart_obj.user = request.user # anonymnus cart gets owner
                cart_obj.accepted = False
                cart_obj.save()
                print('user cart user=NULL converted to req.user',request.user)

        else:
            # inc case of just created user with cart but NO session['cart_id']
            cart_obj = Cart.objects.new(user=request.user,accepted=False)
            print('new cart obj created')
            request.session['cart_id'] = cart_obj.id
            print("session cart-id established",cart_obj.id)
        return cart_obj

    def new(self,user=None,accepted=False):
        print('manager "new" calling: user is ',user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj,accepted=False)



class Cart(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)
    total = models.DecimalField(decimal_places=2,
                        max_digits=10000000,
                        default = 0.00,
                        editable=True)
    active = models.BooleanField(default=True)
    objects = CartManager()

    def __str__(self):
        if self.user:
            return "cart id:{} user:{}".format(self.id,self.user.id)
        return  "cart id:{} anonymnus".format(self.id)
    # def get_sum_items_price(self):
    #     total_price = self.cart_items.aggregate(total_price=Sum('sub_total'))
    #     price = total_price.get('total_price')
    #     return price
    #
    # def get_sum_items_amount(self):
    #     total_qty = self.cart_items.aggregate(total=Sum('qty'))
    #     num_items_cart = total_qty.get('total')
    #     return num_items_cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_in_carts')
    qty = models.PositiveIntegerField(default=0)
    sub_total = models.DecimalField(decimal_places=2,max_digits=10000000)

    def save(self,*args,**kwargs):
        """ generate price for each cart_item"""
        self.sub_total = self.product.price *self.qty
        super().save(*args,**kwargs)


@receiver(pre_save, sender=Product)
def product_presave_receiver(sender, instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = make_unique_slug(instance)
pre_save.connect(product_presave_receiver,sender=Product)

@receiver(post_save,sender = User)
def create_user_cart(sender,instance,created,**kwargs):
    """If New User created, create Cart"""
    if created:
        # let op: id card will be change (ForeignKey)
        cart = Cart.objects.create(user=instance)
        print('new cart with id',cart.id)
