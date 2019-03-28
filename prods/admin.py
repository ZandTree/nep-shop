from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
# from Miele book
# meaning:using ModelInLine for the CartItem model(child model) ==> to include
# if as en inline in the CartAdmin (parent modle)
class CartItemInLine(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']
#vs my owns
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','accepted','total']
    list_filter = []
    #added from Miele
    inlines = [CartItemInLine]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    class Meta:
        model = Product
admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)#,CartItemInLine)
