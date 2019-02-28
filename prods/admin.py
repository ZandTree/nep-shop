from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    class Meta:
        model = Product

admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
